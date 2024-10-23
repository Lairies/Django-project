from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
]
