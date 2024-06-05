from rest_framework import serializers
from project.apps.case.models import Case
from project.apps.case.serializer import CaseSerializer
from project.apps.product.models import Product
from project.apps.product.serializer import ProductSerializer
from project.apps.unique_product.models import UniqueProduct


class UniqueProductSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product')
    case_id = serializers.PrimaryKeyRelatedField(queryset=Case.objects.all(), allow_null=True, source='case')
    product = ProductSerializer(required=False)
    case = CaseSerializer(allow_null=True, required=False)
    class Meta():
        model = UniqueProduct
        fields = ['unique_product_id','product_id','case_id', 'serial_number', 'custom_price', 'status_shipping', 'status_payment',
                  'product', 'case']

    def get_or_create_nested_objects(self, validated_data):
        product_data = validated_data.pop('product')
        product, _ = Product.objects.get_or_create(product_data)

        case_data = validated_data.pop('case', None)
        if case_data:
            case, _ = Case.objects.get_or_create(case_data)
            validated_data['case_id'] = case.id
        else:
            validated_data['case_id'] = None

        validated_data['product_id'] = product.id

        return validated_data

    def create(self, validated_data):
        validated_data = self.get_or_create_nested_objects(validated_data)
        unique_product = UniqueProduct.objects.create(**validated_data)
        return unique_product
