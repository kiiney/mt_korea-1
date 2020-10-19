from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('list/', views.boardlist, name='boardlist'),
    path('list/detail/', views.boardlistdetail, name='boardlist'),
    path('list/detail/<int:pk>/', views.boardlistdetail, name='list_detail'),
]