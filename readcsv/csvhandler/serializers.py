from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': False},
            'description': {'required': False},
        }
