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
    user = UserSerializer(required=False)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user')

    class Meta:
        model = Case
        fields = ['id', 'created_at', 'vessel', 'user', "title", "description", "deadline", "vessel_id", "user_id", "case_status"]

    def get_or_create_nested_objects(self, validated_data):
        vessel_data = validated_data.pop('vessel')
        vessel, _ = Vessel.objects.get_or_create(pk=vessel_data.id)

        validated_data['vessel_id'] = vessel.id

        user = validated_data.pop('user', None)
        if user:
            user, _ = User.objects.get_or_create(pk=user.id)
            validated_data['user_id'] = user.id
        else:
            validated_data['user_id'] = None

        return validated_data

    def create(self, validated_data):
        validated_data = self.get_or_create_nested_objects(validated_data)
        case = Case.objects.create(**validated_data)
        return case
