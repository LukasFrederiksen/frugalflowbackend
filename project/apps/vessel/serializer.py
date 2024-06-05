from rest_framework import serializers
from .models import Vessel
from ..customer.models import Customer
from ..customer.serializer import CustomerSerializer


class VesselSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), source='customer', allow_null=True)
    customer = CustomerSerializer(allow_null=True, required=False)

    class Meta:
        model = Vessel
        fields = ['id', 'name', 'type', 'isDeleted', 'customer', 'customer_id']

    def get_or_create_nested_objects(self, validated_data):
        customer_data = validated_data.pop('customer')
        customer, _ = Customer.objects.get_or_create(pk=customer_data.id)

        validated_data['customer_id'] = customer.id

        return validated_data
    def create(self, validated_data):
        validated_data = self.get_or_create_nested_objects(validated_data)
        vessel = Vessel.objects.create(**validated_data)
        return vessel