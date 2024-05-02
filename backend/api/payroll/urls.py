from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet

from . import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
]
