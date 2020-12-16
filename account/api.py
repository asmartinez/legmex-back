# api.py
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import register_serializer, user_serializer

class register_api(generics.GenericAPIView):
	serializer_class = register_serializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()

		return Response({
				'user': user_serializer(user, context=self.get_serializer_context()).data,
				'message': 'User Create Successfully. Now perform Login to get your token'
			})