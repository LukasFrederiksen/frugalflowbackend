from rest_framework import serializers
from project.apps.case.models import Case
from project.apps.users.models import User
from project.apps.users.serializer import UserSerializer
from project.apps.vessel.models import Vessel
from project.apps.vessel.serializer import VesselSerializer


class CaseSerializer(serializers.ModelSerializer):
    # Nested relationship serializers
    vessel = VesselSerializer(required=False)
    vessel_id = serializers.PrimaryKeyRelatedField(queryset=Vessel.objects.all(), source='vessel')
    case_manager = UserSerializer(required=False)
    case_manager_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user')

    class Meta:
        model = Case
        fields = ['vessel', 'case_manager', "title", "description", "deadline", "vessel_id", "case_manager_id"]

    def get_or_create_nested_objects(self, validated_data):
        vessel_data = validated_data.pop('vessel')
        vessel, _ = Vessel.objects.get_or_create(pk=vessel_data.id)

        validated_data['product_id'] = vessel.id

        case_manager = validated_data.pop('user', None)
        if case_manager:
            user, _ = User.objects.get_or_create(pk=case_manager.id)
            validated_data['case_manager_id'] = case_manager.id
        else:
            validated_data['case_manager_id'] = None

        return validated_data

    def create(self, validated_data):
        validated_data = self.get_or_create_nested_objects(validated_data)
        case = Case.objects.create(**validated_data)
        return case
