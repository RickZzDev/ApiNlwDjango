from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


# Create your views here.
class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.prefetch_related("item").all()
    def get_serializer_class(self):
        if self.request.method == "GET":
           return ReadPointSerializer
        else:
            return CreatePointSerializer   

   


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
