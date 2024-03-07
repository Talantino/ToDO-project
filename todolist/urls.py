from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("add", views.add, name='add'),
    path('update/<int:todo_id>/', views.update, name="update"),
    path('update_button/<int:todo_id>/', views.update_button, name="update_button"),
    path('delete/<int:todo_id>/', views.delete, name="delete"),
]
