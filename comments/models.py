from django.db import models


class User(models.Model):
    """
    Модель для пользователя.
    """
    username = models.CharField(max_length=100, verbose_name="Имя пользователя")
    email = models.EmailField(verbose_name="Электронная почта")

    def __str__(self):
        return self.username


class Comment(models.Model):
    """
    Модель для комментариев.
    """
    username = models.CharField(max_length=100, verbose_name="Имя пользователя")
    email = models.EmailField(verbose_name="Электронная почта")
    text = models.TextField(verbose_name="Текст комментария")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.username} - {self.created_at}"


class File(models.Model):
    """
    Модель для файлов.
    """
    name = models.CharField(max_length=255, verbose_name="Название файла")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")
    file = models.FileField(upload_to="uploads/", verbose_name="Файл")

    def __str__(self):
        return self.name

