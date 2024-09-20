from django.shortcuts import render
from django.http import HttpResponse
from . import models, serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView 
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet 
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated] 
   
class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer