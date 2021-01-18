from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createTodo/', views.createTodo, name="createTodo"),
    path('deletTodo/', views.deletTodo, name="deletTodo"),
    path('clearTodo/', views.clearTodo, name="clearTodo"),
]
