from django.db.models import fields
from core.models import Material
from rest_framework import serializers

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"
        