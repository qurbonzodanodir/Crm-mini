from django.shortcuts import render
from rest_framework import generics
from .serializers import AppealSerializer
from .models import Appeal
from .permissions import IsOperatorOrBackOffice
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend


class AppealApiListView(generics.ListAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['customer_name','account_number','phone_number','status']
    permission_classes = [IsOperatorOrBackOffice,IsAuthenticated]

class AppealApiCreateView(generics.CreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
    permission_classes = [IsOperatorOrBackOffice,IsAuthenticated]


class AppealApiUpdateView(generics.UpdateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
    permission_classes = [IsOperatorOrBackOffice,IsAuthenticated]