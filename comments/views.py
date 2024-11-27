from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from .models import User, Comment, File
from .serializers import UserSerializer, CommentSerializer, FileSerializer


class UserViewSet(ModelViewSet):
    """
    ViewSet для работы с моделью User.
    Позволяет выполнять операции CRUD для пользователей.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentViewSet(ModelViewSet):
    """
    ViewSet для работы с моделью Comment.
    Позволяет выполнять операции CRUD для комментариев.
    Добавлена валидация CAPTCHA через сериализатор.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class FileViewSet(ModelViewSet):
    """
    ViewSet для работы с моделью File.
    Позволяет выполнять операции CRUD для файлов.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer


class CaptchaAPIView(APIView):
    """
    Генерация новой CAPTCHA.
    Клиент получает уникальный ключ и URL изображения для CAPTCHA.
    """
    def get(self, request, *args, **kwargs):
        # Генерация нового ключа CAPTCHA
        captcha_key = CaptchaStore.generate_key()
        image_url = captcha_image_url(captcha_key)

        return Response({
            'captcha_key': captcha_key,
            'captcha_image_url': image_url
        })


