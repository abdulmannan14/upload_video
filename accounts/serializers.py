from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class register_serializer(serializers.Serializer):
    email=serializers.EmailField()
    username= serializers.CharField(max_length=200)
    password=serializers.CharField(max_length=20,min_length=8)



class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)