from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer, EditUserSerializer


class UserRegisterView(APIView):
    def post(self, request: Request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(data={'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditUserView(APIView):
    def put(self, request: Request):
        user_serializer = EditUserSerializer(instance=request.user, data=request.data, context={'request': request}, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(data=user_serializer.data, status=status.HTTP_200_OK)
        return Response(data=user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    def get(self, request: Request):
        request.auth.delete()
        return Response(data={'message': 'you logged out successfully'}, status=status.HTTP_204_NO_CONTENT)
