from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     user = serializers.StringRelatedField(many=False)
#     class Meta:
#         model = models.UserProfile
#         fields = '__all__'

# class RegistrationSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(required = True)
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
    
#     def save(self):
#         username = self.validated_data['username']
#         first_name = self.validated_data['first_name']
#         last_name = self.validated_data['last_name']
#         email = self.validated_data['email']
#         password = self.validated_data['password']
#         password2 = self.validated_data['confirm_password']
        
#         if password != password2:
#             raise serializers.ValidationError({'error' : "Password did't Match!"})
#         if User.objects.filter(email=email).exists():
#             raise serializers.ValidationError({'error' : "This Email Already Exists!"})
#         account = User(username = username, email=email, first_name = first_name, last_name = last_name)
#         print(account)
#         account.set_password(password)
#         account.is_active = False
#         account.save()
#         return account

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.is_active = False  # Set to False if email confirmation is needed
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)

    
#     def save(self):
#         username = self.validated_data['username']
#         first_name = self.validated_data['first_name']
#         last_name = self.validated_data['last_name']
#         email = self.validated_data['email']
#         password = self.validated_data['password']
#         password2 = self.validated_data['confirm_password']
        
#         if password != password2:
#             raise serializers.ValidationError({'error' : "Password Doesn't Mactched"})
#         if User.objects.filter(email=email).exists():
#             raise serializers.ValidationError({'error' : "Email Already exists"})
#         account = User(username = username, email=email, first_name = first_name, last_name = last_name)
#         print(account)
#         account.set_password(password)
#         account.is_active = False
#         account.save()
#         return account


# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField(required = True)
#     password = serializers.CharField(required = True)