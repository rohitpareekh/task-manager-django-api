from rest_framework import serializers
from .models import Task 
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Authentication
#         fields = ['email', 'password']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         try:
#             user = Authentication.objects.get(email=data['email'])
#         except Authentication.DoesNotExist:
#             raise serializers.ValidationError("Invalid email or password")

#         if not check_password(data['password'], user.password):
#             raise serializers.ValidationError("Invalid email or password")

#         data['user'] = user
#         return data  
 
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']      
