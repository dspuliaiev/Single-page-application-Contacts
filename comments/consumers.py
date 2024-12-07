import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer

logger = logging.getLogger(__name__)

class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Определяем имя группы WebSocket
        self.room_group_name = "chat_room"

        # Присоединяемся к группе
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        # Принимаем WebSocket-соединение
        await self.accept()

    async def disconnect(self, close_code):
        # Отключаемся от группы
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    async def broadcast_new_comment(self, event):
        # Получаем сериализованные данные комментария
        comment = event['comment']

        # Логирование перед отправкой комментария на фронт
        logger.info(f"Отправка комментария на фронт: {comment}")

        # Отправляем сообщение всем клиентам, кроме автора
        await self.send(text_data=json.dumps({
            'type': 'new_comment',
            'data': comment,
        }))
