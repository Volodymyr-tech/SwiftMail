from django.urls import path
from django.views.generic import CreateView

from clients.views import HomeView

app_name = 'clients'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-client', CreateView.as_view(), name='add-client'),

]

