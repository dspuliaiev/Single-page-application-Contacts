from django import forms
from captcha.fields import CaptchaField
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Форма для модели Comment с добавлением CAPTCHA.
    """
    captcha = CaptchaField(label="Введите CAPTCHA")

    class Meta:
        model = Comment
        fields = ['username', 'email', 'text', 'captcha']
