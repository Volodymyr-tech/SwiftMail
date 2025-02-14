from django.urls import path
from message.views import MessageListView, CreateMessageView, ReadMessageView, UpdateMessageView, DeleteMessageView

app_name = 'message'

urlpatterns = [
    path('list/', MessageListView.as_view(), name='list'),
    path('add_message/', CreateMessageView.as_view(), name='add-message'),
    path('delete_message/<int:pk>', DeleteMessageView.as_view(), name='delete-message'),
    path('update_message/<int:pk>', UpdateMessageView.as_view(), name='update-message'),
    path('detail_message/<int:pk>', ReadMessageView.as_view(), name='detail-message'),

]

