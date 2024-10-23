from django.urls import path
from . import views

app_name = 'app2'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('welcome/', views.welcome, name='welcome'),
]
