from rest_framework import serializers
from .models import Comment, ClientInfo

class CommentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id', 'user_name', 'email', 'text', 'created_at', 'active',
            'updated_at', 'home_page', 'captcha', 'image', 'text_file',
            'parent_comment', 'client_info', 'children'
        ]

    def get_children(self, obj):
        # Получаем дочерние комментарии
        children = Comment.objects.filter(parent_comment=obj)
        # Рекурсивно сериализуем их
        return CommentSerializer(children, many=True).data

class ClientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientInfo
        fields = ['ip_address', 'user_agent', 'user_name']

