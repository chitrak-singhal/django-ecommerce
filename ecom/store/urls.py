from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),#homepage url
    path('test', views.test, name='test'),
]