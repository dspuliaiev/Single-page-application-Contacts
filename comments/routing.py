from django.urls import path
from . import consumers

app_name = "comments"

websocket_urlpatterns = [
    path('ws/chat/', consumers.ChatConsumer.as_asgi()),
]
