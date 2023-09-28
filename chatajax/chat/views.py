from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from chat.models import Room, Message
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MessageSerializer, RoomSerializer
from rest_framework import viewsets
from rest_framework import permissions


# class ChatView(APIView):
#     def post(self, request):
#         serializer = MessageSerializer(data=request.data)
#         if serializer.is_valid():
#             message = serializer.validated_data['message']
#
#             channel_layer = get_channel_layer()
#             async_to_sync(channel_layer.group_layer)('room', {
#                 'type': 'message',
#                 'message': message
#             })
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def chat_box(request, room_title):
    return render(request, "chat.html", {'room_title': room_title})


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


# class Chat(LoginRequiredMixin, CreateView):
#     model = Message
#     ordering = 'data'
#     form_class = SendMessage
#     template_name ='chat.html'
#     context_object_name = 'chat'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['messages'] = Message.objects.all()
#         return context
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         room_id = form.cleaned_data['room']
#         form.instance.room_id = room_id
#
#         return super().form_valid(form)
#
#     def get(self, request, room_title):
#         return render(request, 'chat.html', {'room_title': room_title})
