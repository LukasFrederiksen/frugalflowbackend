from rest_framework import serializers
from .models import Customer
from ..case.models import Case


class CustomerSerializer(serializers.ModelSerializer):
    # cases = serializers.PrimaryKeyRelatedField(many=True, queryset=Case.objects.all())

    class Meta:
        model = Customer
        fields = ['id', 'name', 'description', 'email', 'phone', 'address', 'customer_picture']
        

