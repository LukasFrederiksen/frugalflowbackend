from rest_framework import serializers
from .models import Manufacture
from ..contacts.models import ContactPerson
from ..contacts.serializer import ContactPersonSerializer


class ManufactureSerializer(serializers.ModelSerializer):
    contact_person_id = serializers.PrimaryKeyRelatedField(queryset=ContactPerson.objects.all(), source='contact_person', allow_null=True)
    contact_person = ContactPersonSerializer(allow_null=True, required=False)

    class Meta:
        model = Manufacture
        fields = ['id', 'cvr', 'name', 'contact_person', 'contact_person_id', 'phone', 'email', 'website', 'picture_logo', 'is_deleted']

    def get_or_create_nested_objects(self, validated_data):
        contact_person_data = validated_data.pop('contact_person')
        contact_person, _ = ContactPerson.objects.get_or_create(pk=contact_person_data.id)

        validated_data['contact_person_id'] = contact_person.id

        return validated_data
    def create(self, validated_data):
        validated_data = self.get_or_create_nested_objects(validated_data)
        manufacture = Manufacture.objects.create(**validated_data)
        return manufacture