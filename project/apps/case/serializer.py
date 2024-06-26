from rest_framework import serializers

from project.apps.case.models import Case, CaseProduct
from project.apps.customer.serializer import CustomerSerializer
from project.apps.users.models import User
from project.apps.users.serializer import UserSerializer


class CaseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseProduct
        fields = '__all__'  # This will include all fields in the serializer


class CaseSerializer(serializers.ModelSerializer):
    # Nested relationship serializers
    followers = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    vessel = serializers.StringRelatedField()
    product_owner = serializers.StringRelatedField()
    customer_data = CustomerSerializer(source='customer', read_only=True, many=False)
    case_products = CaseProductSerializer(many=True, read_only=True)

    def create(self, validated_data):
        followers_data = validated_data.pop('followers', [])
        case = Case.objects.create(**validated_data)
        case.followers.set(followers_data)  # Set the followers
        return case

    class Meta:
        model = Case
        fields = '__all__'



