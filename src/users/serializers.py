from rest_framework import serializers
#from django.contrib.auth.models import User
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'nombre',
            'apellido'
        )

'''class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

        class Meta:
            model = User
            fields = ('id', 'username', 'password')
            extra_kwargs = {
                'password': {'write_only': True}
            }'''
