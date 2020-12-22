from django.urls import path
from django.contrib.auth.decorators import login_required
from main import views

urlpatterns = [
    path('index/', views.index),
    path('mainpage/', login_required(views.home), name='home'),
]