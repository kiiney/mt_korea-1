from django.contrib import admin
from django.urls import path, include

from . import views
app_name = 'board'

urlpatterns = [
    path('', views.index),
    path('list/', views.boardlist, name='boardlist'),
    path('list/detail/<str:NAME>', views.boardview, name='boardview'),
]