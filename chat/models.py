import uuid

from django.db import models

from user.models import User


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user1 = models.ForeignKey(User, related_name='author_room', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='friend_room', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user1}-{self.user2}"


class Chat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='chats')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_msg')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_msg')
    text = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    has_seen = models.BooleanField(default=False)

    def __str__(self):
        return '%s - %s' % (self.id, self.date)
