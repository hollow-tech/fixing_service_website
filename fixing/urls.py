from django.urls import path
from .views import AddOrder, home, AddConsultation

app_name = 'fixing'
urlpatterns = [
    path('', home, name='home'),
    path('order/', AddOrder, name='order'),
    path('consultation/', AddConsultation, name='consultation')
]