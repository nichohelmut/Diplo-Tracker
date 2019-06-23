from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index),
    path('new', views.new, name='plate_new'),
    path('', views.overview)
]