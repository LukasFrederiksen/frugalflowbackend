from rest_framework import serializers
from .models import UniqueProduct
from project.apps.manufacture.serializer import ManufactureSerializer


class ProductSerializer(serializers.ModelSerializer):
    manufacturer = ManufactureSerializer(read_only=True)

    class Meta:
        model = UniqueProduct
        fields = '__all__'
