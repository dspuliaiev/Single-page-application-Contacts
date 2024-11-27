from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CommentViewSet, FileViewSet, CaptchaAPIView

# Маршруты для API
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'files', FileViewSet, basename='file')

urlpatterns = [
    # Эндпоинт для генерации CAPTCHA
    path('captcha/', CaptchaAPIView.as_view(), name='captcha'),
    # Включение маршрутов от DRF
    path('', include(router.urls)),
]

