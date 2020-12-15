from django.urls import path
from . import views



urlpatterns = [
    path('', views.atendimentos_list, name='atendimentos_list'),
]