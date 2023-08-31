from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .serializers import UserRegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


# Create your views here.
@api_view(['POST'])
def user_registration_view(request):
    
    serializer = UserRegistrationSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        refresh_token = RefreshToken.for_user(user)

        return Response({'refresh_token' : str(refresh_token), 'access_token' : str(refresh_token.access_token) }, status= status.HTTP_201_CREATED)
    
    return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
