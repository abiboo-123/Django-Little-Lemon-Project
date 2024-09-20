from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class MenuItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.MenuItem
        fields = '__all__'  

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = '__all__'
    

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']