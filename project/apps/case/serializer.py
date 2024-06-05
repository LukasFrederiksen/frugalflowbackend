from rest_framework import serializers
from project.apps.case.models import Case
from project.apps.users.serializer import UserSerializer
from project.apps.vessel.serializer import VesselSerializer


class CaseSerializer(serializers.ModelSerializer):
    # Nested relationship serializers
    vessel = VesselSerializer()
    case_manager = UserSerializer()

    def create(self, validated_data):
        case = Case.objects.create(**validated_data)
        return case

    class Meta:
        model = Case
        fields = '__all__'
