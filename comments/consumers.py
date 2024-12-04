import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Comment
from .serializers import CommentSerializer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            'message': 'WebSocket connection established',
        }))
        await self.send_comments_list()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get('action')

        if action == 'create_comment':
            await self.create_comment(data)
        elif action == 'list_comments':
            await self.send_comments_list()

    @database_sync_to_async
    def get_comments_from_db(self):
        comments = Comment.objects.all().order_by('-created_at')
        return CommentSerializer(comments, many=True).data

    async def send_comments_list(self):
        comments = await self.get_comments_from_db()
        await self.send(text_data=json.dumps({
            'action': 'list_comments',
            'comments': comments,
        }))

    @database_sync_to_async
    def create_comment_in_transaction(self, data):
        comment = Comment.objects.create(
            user_name=data.get('user_name'),
            email=data.get('email'),
            text=data.get('text'),
            home_page=data.get('home_page'),
            captcha=data.get('captcha'),
            image=data.get('image'),
            text_file=data.get('text_file'),
            parent_comment_id=data.get('parent_comment_id'),
        )
        return CommentSerializer(comment).data

    async def create_comment(self, data):
        new_comment = await self.create_comment_in_transaction(data)
        await self.send_comments_list()
        await self.channel_layer.group_send(
            'chat_group',
            {
                'type': 'broadcast_comments',
                'comment': new_comment,
            }
        )

    async def broadcast_comments(self, event):
        comment = event['comment']
        await self.send(text_data=json.dumps({
            'action': 'new_comment',
            'comment': comment,
        }))