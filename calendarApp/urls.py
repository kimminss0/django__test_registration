from django.urls import path
from . import views

urlpatterns = [
    path('', views.CalList.as_view()),
    path('/<int:pk>', views.CalDetail.as_view()),
]