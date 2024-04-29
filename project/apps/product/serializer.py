from rest_framework import serializers
from .models import Product
from project.apps.manufacture.serializer import ManufactureSerializer


class ProductSerializer(serializers.ModelSerializer):
    manufacturer = ManufactureSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
