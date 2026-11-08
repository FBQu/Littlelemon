from rest_framework import serializers

from .models import MenuModel, BookingModel

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModel
        fields = '__all__'

class MenuSerialzer(serializers.ModelSerializer):
    class Meta:
        model = MenuModel
        fields = '__all__'