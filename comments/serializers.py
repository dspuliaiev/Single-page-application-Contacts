from rest_framework import serializers
from captcha.models import CaptchaStore
from .models import User, Comment, File


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Comment.
    Добавлена валидация CAPTCHA.
    """
    captcha_key = serializers.CharField(
        write_only=True,
        required=True,
        help_text="Уникальный ключ для проверки CAPTCHA"
    )
    captcha_value = serializers.CharField(
        write_only=True,
        required=True,
        help_text="Значение CAPTCHA, введенное пользователем"
    )

    class Meta:
        model = Comment
        fields = ['id', 'username', 'email', 'text', 'created_at', 'captcha_key', 'captcha_value']

    def validate(self, data):
        """
        Проверка CAPTCHA: сопоставление ключа и значения.
        """
        captcha_key = data.get('captcha_key')
        captcha_value = data.get('captcha_value')

        if not captcha_key or not captcha_value:
            raise serializers.ValidationError("CAPTCHA обязательна для заполнения.")

        # Проверяем, существует ли CAPTCHA с указанным ключом
        try:
            captcha = CaptchaStore.objects.get(hashkey=captcha_key)
        except CaptchaStore.DoesNotExist:
            raise serializers.ValidationError("Указанная CAPTCHA устарела или неверна.")

        # Сравниваем введенное значение с оригиналом
        if captcha.response != captcha_value.lower():
            raise serializers.ValidationError("CAPTCHA введена неверно.")

        # Удаляем CAPTCHA после успешной проверки
        captcha.delete()
        return data


class FileSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели File.
    """
    class Meta:
        model = File
        fields = ['id', 'name', 'uploaded_at', 'file']


