from rest_framework import serializers
from .models import Product, SimpleProduct
from project.apps.manufacture.serializer import ManufactureSerializer
from .models import UniqueProduct
from ..case.models import Case
from ..case.serializer import CaseSerializer


class ProductSerializer(serializers.ModelSerializer):
    manufacture = ManufactureSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['name', 'description', 'cost_price', 'retail_price', 'is_deleted', 'manufacture', 'sku', 'is_unique']


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

class UniqueProductSerializer(ProductSerializer):
    product = ProductSerializer()
    case = CaseSerializer(allow_null=True)

    class Meta(ProductSerializer.Meta):
        model = UniqueProduct
        fields = ['unique_product_id', 'product', 'serial_number', 'custom_price', 'status_shipping', 'status_payment', 'case']

    def get_or_create_nested_objects(self, validated_data):
        product_data = validated_data.pop('product')
        product, _ = Product.objects.get_or_create(**product_data)

        case_data = validated_data.pop('case', None)
        if case_data:
            case, _ = Case.objects.get_or_create(**case_data)
            validated_data['case_id'] = case.id
        else:
            validated_data['case_id'] = None

        validated_data['product_id'] = product.id

        return validated_data

    def create(self, validated_data):
        validated_data = self.get_or_create_nested_objects(validated_data)
        unique_product = UniqueProduct.objects.create(**validated_data)
        return unique_product


# class UniqueProductSerializer(ProductSerializer):
#     product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)
#     case_id = serializers.PrimaryKeyRelatedField(queryset=Case.objects.all(), write_only=True, allow_null=True)
#     class Meta(ProductSerializer.Meta):
#         model = UniqueProduct
#         fields = ['unique_product_id', 'product_id', 'serial_number', 'custom_price', 'status_shipping', 'status_payment', 'case_id']
#
#     def create(self, validated_data):
#         product = validated_data.pop('product_id')
#         validated_data['product_id'] = product.id
#         case = validated_data.pop('case_id')
#         if case is not None:
#             validated_data['case_id'] = case.id
#         else:
#             validated_data['case_id'] = None
#         unique_product = UniqueProduct.objects.create(**validated_data)
#         return unique_product
