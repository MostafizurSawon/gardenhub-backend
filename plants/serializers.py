from rest_framework import serializers
from . import models

class PlantSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    # category = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Plant
        fields = ['title', 'price', 'category', 'user', 'image', 'description', 'quantity', 'created']  # Exclude 'sold'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
        
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'
