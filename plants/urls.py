from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter() # amader router

router.register('plant-list', views.PlantViewset) # router er antena
router.register('category', views.CategoryViewset)
router.register('reviews', views.ReviewViewset) 

urlpatterns = [
    path('', include(router.urls)),
]