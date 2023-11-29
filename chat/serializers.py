from rest_framework import serializers

from chat.models import Chat
from user.serializers import UserSerializer


class ChatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'author', 'friend', 'text', 'date', 'has_seen')

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #
    #     # 'author' va 'friend' uchun foydalanuvchi obyektlarini olish
    #     author_data = UserSerializer(instance.author).data
    #     friend_data = UserSerializer(instance.friend).data
    #
    #     # O'zgartirilgan ma'lumotlarni qo'shish
    #     representation['author'] = author_data
    #     representation['friend'] = friend_data
    #
    #     return representation
