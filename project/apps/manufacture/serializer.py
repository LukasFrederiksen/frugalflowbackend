from rest_framework import serializers
from .models import Manufacture
from ..contacts.serializer import ContactPersonSerializer


class ManufactureSerializer(serializers.ModelSerializer):
    contactperson = ContactPersonSerializer()

    class Meta:
        model = Manufacture
        fields = ['id', 'cvr', 'name', 'contactperson', 'phone', 'email', 'website', 'picture_logo', 'isdeleted']
