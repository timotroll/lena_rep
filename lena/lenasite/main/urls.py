from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='house'),
    path('about/', views.about, name='about'),
    path('request/', views.register, name='register')
]