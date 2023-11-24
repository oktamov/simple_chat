from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from user.serializers import UserSerializer
from .models import Room, Chat
from django.contrib.auth.models import User
from .serializers import ChatsSerializer


class FriendsListView(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        friend_rooms = Room.objects.filter(user1=user) | Room.objects.filter(user2=user)
        friends_data = []

        for room in friend_rooms:
            friend_data = {}

            if room.user1 == user:
                friend_data['friend_id'] = room.user2.id
                friend_data['friend_info'] = UserSerializer(room.user2).data
            else:
                friend_data['friend_id'] = room.user1.id
                friend_data['friend_info'] = UserSerializer(room.user1).data

            friend_data['room_id'] = room.id
            friends_data.append(friend_data)

        return Response(friends_data, status=status.HTTP_200_OK)


class MessagesView(generics.ListAPIView):
    serializer_class = ChatsSerializer

    def get_queryset(self):
        user = self.request.user
        room_id = self.kwargs.get('room_id')
        room = Room.objects.get(id=room_id)

        if user == room.user1 or user == room.user2:
            messages = (Chat.objects.filter(author=room.user1, friend=room.user2) |
                        Chat.objects.filter(author=room.user2, friend=room.user1)).order_by('-date')

            return messages
        return Chat.objects.none()
