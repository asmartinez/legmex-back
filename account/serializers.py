# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

class register_serializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'email', 'password', 'username')  # the value 'name' return an error :
		extra_fields = {'password': {'write_only': True}}

	def create(self, validated_data):
		user = User.objects.create_user(
				email=validated_data['email'],
				password=validated_data['password'],
				username=validated_data['username'])
		return user

class user_serializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'