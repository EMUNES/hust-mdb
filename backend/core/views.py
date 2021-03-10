from django.shortcuts import render
from core.models import Material
from core.serializers import MaterialSerializer
from rest_framework import generics

# Create your views here.

class MaterialList(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
