from django.urls import path
from . import views

app_name = 'recompensa'

urlpatterns = [
    path('', views.recompensa, name='recompensa')
]