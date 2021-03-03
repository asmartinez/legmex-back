from django.contrib.auth import password_validation, authenticate

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'is_client',
            'is_verfied',

        )

class UserLoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('El usuario no es valido')

        self.context['persona'] = user
        return data

    def create(self, data):
        """Generar o recuperar token"""
        token, created = Token.objects.get_or_create(user=self.context['persona'])
        return self.context['persona'], token.key



