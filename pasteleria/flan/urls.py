from django.urls import path
from . import views
from .views import home, index




urlpatterns=[
    path('', views.home, name='home'),
    path('fla', views.index, name='index'),
    
]