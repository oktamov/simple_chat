from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from chat.models import Room, Chat
from user.models import User


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})


@login_required
def chatroom(request, room_name, friend_id):
    all_rooms = Room.objects.filter(id=room_name)
    if not all_rooms:
        messages.error(request, 'Invalid Room ID')
        return redirect('room-enroll')

    chats = Chat.objects.filter(
        room_id=room_name
    ).order_by('date')

    context = {
        'old_chats': chats,
        'my_name': request.user,
        'friend_name': User.objects.get(pk=friend_id),
        'room_name': room_name
    }
    return render(request, 'chat/chatroom.html', context)
