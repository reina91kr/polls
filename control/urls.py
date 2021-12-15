from django.urls import path
from control import views

app_name = 'control'

urlpatterns = [
    path('', views.index, name='index'),       #127.0.0.1:8000/control
    path('register/', views.register, name ="register")
]
