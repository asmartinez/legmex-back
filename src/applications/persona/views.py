from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)

from .models import User

from .serializer import UserSerializer

# Create your views here.

class UserListApiView(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    



