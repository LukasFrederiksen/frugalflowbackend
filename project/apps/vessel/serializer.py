from rest_framework import serializers
from .models import Vessel
from ..customer.serializer import CustomerSerializer


class VesselSerializer(serializers.ModelSerializer):
    vessel_owner = CustomerSerializer()
    class Meta:
        model = Vessel
        fields = '__all__'
