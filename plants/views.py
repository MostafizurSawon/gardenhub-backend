from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission

class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    

# class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
#     def filter_queryset(self, request, query_set, view):
#         doctor_id = request.query_params.get("doctor_id")
#         if doctor_id:
#             return query_set.filter(doctor = doctor_id)
#         return query_set

# class AvailableTimeViewset(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = models.AvailableTime.objects.all()
#     serializer_class = serializers.AvailableTimeSerializer
#     filter_backends = [AvailableTimeForSpecificDoctor]

class PlantPagination(pagination.PageNumberPagination):
    page_size = 10 # items per page
    page_size_query_param = page_size
    max_page_size = 100

class PlantViewset(viewsets.ModelViewSet):
    queryset = models.Plant.objects.all()
    serializer_class = serializers.PlantSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = PlantPagination
    search_fields = [
        'title',                  # Plant title
        'description',            # Plant description
        'category__name',         # Category name
        'user__first_name',       # User's first name
        'user__last_name',        # User's last name
        'user__username',         # User's username
        'user__email',            # User's email
        'comments__user__username',  # Comment user username
    ]
    # permission_classes = [IsAuthenticated]  # Enforce authentication

    def perform_create(self, serializer):
        # Assign the current user as the owner of the Plant
        # serializer.save(user=self.request.user)
        serializer.save()
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer