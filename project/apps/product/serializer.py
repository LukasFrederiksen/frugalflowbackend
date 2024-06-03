from rest_framework import serializers
from .models import Product, SimpleProduct
from project.apps.manufacture.serializer import ManufactureSerializer
from .models import UniqueProduct
from ..case.models import Case


class ProductSerializer(serializers.ModelSerializer):
    manufacturer = ManufactureSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'description', 'cost_price', 'retail_price', 'is_deleted', 'manufacture_id', 'sku', 'is_unique']


class SimpleProductSerializer(ProductSerializer):
    case_id = serializers.PrimaryKeyRelatedField(queryset=Case.objects.all(), write_only=True)
    class Meta(ProductSerializer.Meta):
        model = SimpleProduct
        fields = ProductSerializer.Meta.fields + ['case_id', 'qty']

    def create(self, validated_data):
        print(validated_data)
        case_id = validated_data.pop('case_id')
        simple_product = SimpleProduct.objects.create(**validated_data)
        simple_product.case.set([case_id])
        return simple_product


class UniqueProductSerializer(ProductSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)

    class Meta(ProductSerializer.Meta):
        model = UniqueProduct
        fields = ['product_id', 'serial_number', 'custom_price', 'status_shipping', 'status_payment']

    def create(self, validated_data):
        print(validated_data)
        case_id = validated_data.pop('product_id')
        unique_product = UniqueProduct.objects.create(**validated_data)
        unique_product.case.set([case_id])
        return unique_product
