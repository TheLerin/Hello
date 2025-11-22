from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send/', views.send_message, name='send_message'),
    path('get/', views.get_messages, name='get_messages'),
]