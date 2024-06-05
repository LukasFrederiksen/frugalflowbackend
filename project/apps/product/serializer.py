from rest_framework import serializers
from .models import Product, SimpleProduct
from project.apps.manufacture.serializer import ManufactureSerializer
from ..case.serializer import CaseSerializer


class ProductSerializer(serializers.ModelSerializer):
    manufacture = ManufactureSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'cost_price', 'retail_price', 'is_deleted', 'manufacture', 'sku',
                  'is_unique']


class SimpleProductSerializer(ProductSerializer):
    case = CaseSerializer(allow_null=True)

    # case_id = serializers.PrimaryKeyRelatedField(queryset=Case.objects.all(), write_only=True)
    class Meta(ProductSerializer.Meta):
        model = SimpleProduct
        fields = ProductSerializer.Meta.fields + ['case', 'qty']

    def create(self, validated_data):
        print(validated_data)
        case = validated_data.pop('case_id')
        validated_data['case_id'] = case.id
        simple_product = SimpleProduct.objects.create(**validated_data)
        return simple_product

