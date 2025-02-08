from django.urls import path
from clients.views import HomeView, AddClientView, DeleteClientView, UpdateClientView, DetailClientView

app_name = 'clients'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-client/', AddClientView.as_view(), name='add-client'),
    path('delete-client/', DeleteClientView.as_view(), name='delete-client'),
    path('update-client/', UpdateClientView.as_view(), name='update-client'),
    path('detail-client/<str:pk>', DetailClientView.as_view(), name='detail-client')

]

