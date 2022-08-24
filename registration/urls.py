from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('register/redirect', views.reg_redirect, name='reg_redirect'),
    path('logout', views.logout, name='logout'),
]