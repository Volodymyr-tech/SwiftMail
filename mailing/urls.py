from django.urls import path
from mailing.views import MailListView, AddMailView, UpdateMailView, DeleteMailView, DetailMailView, start_mailing, \
    AllMailListView, stop_mailing

app_name = 'mailing'

urlpatterns = [
    path('mails-list/', MailListView.as_view(), name='list'),
    path('all-mail/', AllMailListView.as_view(), name='all_mail'),
    path('add-mail/', AddMailView.as_view(), name='add-mail'),
    path('delete-mail/<int:pk>', DeleteMailView.as_view(), name='delete-mail'),
    path('update-mail/<int:pk>', UpdateMailView.as_view(), name='update-mail'),
    path('detail-mail/<int:pk>', DetailMailView.as_view(), name='detail-mail'),
    path('start-mail/<int:pk>', start_mailing, name='start_mail'),
    path('stop-mailing/<int:pk>', stop_mailing, name='stop_mailing'),

]

