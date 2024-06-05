from rest_framework import serializers
from .models import Product, SimpleProduct
from project.apps.manufacture.serializer import ManufactureSerializer
from ..case.models import Case
from ..case.serializer import CaseSerializer
from ..manufacture.models import Manufacture


class ProductSerializer(serializers.ModelSerializer):
    manufacture = ManufactureSerializer(required=False)
    manufacture_id = serializers.IntegerField(required=False)
    qty = serializers.IntegerField(required=False, write_only=True, allow_null=True)
    case_id = serializers.PrimaryKeyRelatedField(queryset=Case.objects.all(), write_only=True, allow_null=True,
                                                 required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'cost_price', 'retail_price', 'is_deleted', 'manufacture', 'sku',
                  'is_unique', 'qty', 'case_id', 'manufacture_id']

    def create(self, validated_data):
        qty = validated_data.pop('qty', None)
        case_id = validated_data.pop('case_id', None)
        manufacture_id = validated_data.pop('manufacture_id', None)

        if manufacture_id:
            manufacture = Manufacture.objects.get(pk=manufacture_id)
            validated_data['manufacture'] = manufacture

        if not validated_data['is_unique']:
            SimpleProduct.objects.create(
                product_ptr=validated_data['product_ptr'],
                case_id=validated_data['case_id'],
                qty=validated_data['qty']
            )

        return validated_data


class SimpleProductSerializer(ProductSerializer):
    case = CaseSerializer(allow_null=True, required=False)

    class Meta(ProductSerializer.Meta):
        model = SimpleProduct
        fields = ProductSerializer.Meta.fields + ['case', 'case_id', 'qty']

    def create(self, validated_data):
        validated_data = self.get_or_create_nested_objects(validated_data)
        simple_product = SimpleProduct.objects.create(**validated_data)
        return simple_product

    def get_or_create_nested_objects(self, validated_data):
        case_id = validated_data.pop('case_id', None)
        if case_id:
            case = Case.objects.get(pk=case_id.id)
            validated_data['case'] = case
        return validated_data
