from django.urls import path
from . import views

name_app = 'home'

urlpatterns = [
    path('', views.index, name='index'),
]