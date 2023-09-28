from django.urls import re_path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from chatajax.chat.consumers import *

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_title>\w+)/$", ChatConsumer.as_asgi()),
]

application = ProtocolTypeRouter(
    {
        'websocket': AuthMiddlewareStack(
            URLRouter(
                websocket_urlpatterns
            )
        )
    }
)
