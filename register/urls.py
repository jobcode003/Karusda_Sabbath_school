from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_member, name='register_member'),
    path('register/', views.register_member, name='register_member'),
]
