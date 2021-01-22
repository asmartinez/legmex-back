from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

import requests

from .serializers import CreateUserSerializer


CLIENT_ID = 'HRyEKuSO87Yq8vozVv2pVfqCZc92GWGXHhEjmZ3a'
CLIENT_SECRET = 'NWWbCyHvIsDjUdQQivuCWAejtXLOJXsv8q35AG6XJuRKGsJOFHN7AoefzwrPWYFn9XNv81qyFe6dyCHH7BmIUIE3mjbsidWeYzMIbpMhzThwBqXDxzzIcluUZQQMIw1W'
MiDEBUG = False


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    '''
    Registers user to the server. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    # Put the data from the request into the serializer 
    serializer = CreateUserSerializer(data=request.data) 
    # Validate the data
    if serializer.is_valid():
        # If it is valid, save the data (creates a user).
        serializer.save() 
        # Then we get a token for the created user.
        # This could be done differentley 
        if miDEBUG:
            r = requests.post('https://pycolegiotest.herokuapp.com/:8000/o/token/', data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
            )
        else:
            r = requests.post('https://localhost:8000/o/token/', data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
            )

        return Response(r.json())
    return Response(serializer.errors)



@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    '''
    Gets tokens with username and password. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    if miDEBUG:
        r = requests.post('https://pycolegiotest.herokuapp.com/:8000/o/token/', 
            data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
    else:
        r = requests.post('https://localhost:8000/o/token/', 
            data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
    return Response(r.json())



@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    '''
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    '''
    if miDEBUG:
        r = requests.post('https://pycolegiotest.herokuapp.com/:8000/o/token/', 
            data={
                'grant_type': 'refresh_token',
                'refresh_token': request.data['refresh_token'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
    else:
        r = requests.post('https://localhost:8000/o/token/', 
            data={
                'grant_type': 'refresh_token',
                'refresh_token': request.data['refresh_token'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )

    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    '''
    Method to revoke tokens.
    {"token": "<token>"}
    '''
    if miDEBUG:
        r = requests.post('https://pycolegiotest.herokuapp.com/:8000/o/token/', 
            data={
                'token': request.data['token'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
    else:
        r = requests.post('https://localhost:8000/o/token/', 
            data={
                'token': request.data['token'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )

    # If it goes well return sucess message (would be empty otherwise) 
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    # Return the error if it goes badly
    return Response(r.json(), r.status_code)

'''from django.shortcuts import render
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer'''