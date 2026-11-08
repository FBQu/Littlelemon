from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import BookingModel, MenuModel
from .serializers import BookingSerializer, MenuSerialzer

# Create your views here.\
class MenuItemView(generics.ListCreateAPIView):
    queryset=MenuModel.objects.all()
    serializer_class = MenuSerialzer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset=MenuModel.objects.all()
    serializer_class = MenuSerialzer

class BookingView(viewsets.ModelViewSet):
    queryset=BookingModel.objects.all()
    serializer_class=BookingSerializer
    permission_classes=[IsAuthenticated]