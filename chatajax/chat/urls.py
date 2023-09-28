from django.urls import path
from .views import *


urlpatterns = [
    path('chat/<str:room_title>/', chat_box, name="chat")
    # path('messages/<str:room_title>/', ChatView.as_view()),
    # path('rooms/', send),
    # path('receive/', receive),
    #
    # path('join/', join),
    # path('leave/', leave),
]