from rest_framework import serializers
from .models import Product, SimpleProduct
from project.apps.manufacture.serializer import ManufactureSerializer
from .models import UniqueProduct


class ProductSerializer(serializers.ModelSerializer):
    manufacturer = ManufactureSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class SimpleProductSerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        model = SimpleProduct
        fields = '__all__'


class UniqueProductSerializer(ProductSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)

    class Meta(ProductSerializer.Meta):
        model = UniqueProduct
        fields = ['product_id', 'serial_number', 'custom_price', 'status_shipping', 'status_payment', "is_unique"]



