from accounts.permissions import IsSuperUserOrReadOnly
from django.shortcuts import render
from .serializers import UserRegistrationSerializer, UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
class UserRegistrationApiView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()


class UsersRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSuperUserOrReadOnly,)
    serializer_class = UserSerializer
    queryset = User.objects.all()