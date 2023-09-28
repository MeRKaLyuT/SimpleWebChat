"""
URL configuration for chatajax project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from chat import views
from chat import consumers


router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewSet)
router.register(r'rooms', views.RoomViewSet)

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_title>\w+)/$', consumers.ChatConsumer.as_asgi()),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/', include(router.urls), name='default'),
    path('api-auth', include('rest_framework.urls')),
    path('ws/', include(websocket_urlpatterns)),
]
