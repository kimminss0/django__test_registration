# from django.urls import path
from .views import calViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'calendars', calViewSet, basename='calendars')