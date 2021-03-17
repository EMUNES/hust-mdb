from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from core.models import Material
from core.serializers import MaterialSerializer, UserSerializer

# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        "users": reverse("user-list", request=request, format=format),
        "materials": reverse("material-list", request=request, format=format)
    })


class MaterialList(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    
    filterset_fields = {
        "series": ["icontains"],
        "mark": ["icontains"],
        "manufacturer": ["icontains"],
        "acronym": ["icontains"],
        "material_type": ["icontains"],
        "data_source": ["icontains"],
        "material_id": ["icontains"],
        "level_code": ["icontains"],
        "vendor_code": ["icontains"],
        "fibre_or_infill": ["contains"],
    }
    
    search_fields = [
        "series",
        "mark",
        "manufacturer",
        "acronym",
        "material_type",
        "data_source",
        "material_id",
        "level_code",
        "vendor_code",
        "fibre_or_infill",]
        

class MaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    