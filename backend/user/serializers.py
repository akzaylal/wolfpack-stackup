from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from django import forms
from rest_framework import serializers

class UserRegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    class Meta:
        model = get_user_model()
        fields = ['username','password']
        
    