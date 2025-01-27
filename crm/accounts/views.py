from django.shortcuts import render
from .serializers import CustomUserSerializer
from rest_framework import generics
from .models import Customuser
from rest_framework.permissions import IsAdminUser

class CustomerApiListCreateView(generics.ListCreateAPIView):
    queryset = Customuser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]

class CustomerApiUpdateView(generics.UpdateAPIView):
    queryset = Customuser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]
