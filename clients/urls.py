from django.urls import path
from clients.views import HomeView, AddClientView, DeleteClientView, UpdateClientView, DetailClientView, ClientListView, \
    AllClientsListView

app_name = 'clients'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('list/', ClientListView.as_view(), name='list'),
    path('all-clients/', AllClientsListView.as_view(), name='all_clients'),
    path('add-client/', AddClientView.as_view(), name='add-client'),
    path('delete-client/<int:pk>', DeleteClientView.as_view(), name='delete-client'),
    path('update-client/<int:pk>', UpdateClientView.as_view(), name='update-client'),
    path('detail-client/<int:pk>', DetailClientView.as_view(), name='detail-client')

]

