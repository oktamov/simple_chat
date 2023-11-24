from rest_framework import serializers

from chat.models import Chat


class ChatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'author', 'friend', 'text', 'date', 'has_seen')
