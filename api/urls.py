from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import  include
from .views import RestaurantViewSet, RatingViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('restaurants', RestaurantViewSet)
router.register('ratings', RatingViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

