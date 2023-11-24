from django.urls import path

from . import views
from .rest_view import FriendsListView, MessagesView

urlpatterns = [
    path("", views.index, name="index"),
    # path("<str:room_name>/", views.room, name="room"),
    path('room/<uuid:room_name>/<int:friend_id>', views.chatroom, name='room'),

]

rest = [
    path('friends/', FriendsListView.as_view(), name='friends-list'),
    path('message/<uuid:room_id>/', MessagesView.as_view(), name='messages-list'),
]

urlpatterns += rest
