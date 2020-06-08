from rest_framework import serializers
from .models import *


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'



class CreatePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = '__all__'

class ReadPointSerializer(CreatePointSerializer):
    itens = ItemSerializer(many=True, source = "item")





