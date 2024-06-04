from rest_framework import serializers
from .models import ContactPerson


class ContactPersonSerializer(serializers.ModelSerializer):

   
   class Meta:
       model  = ContactPerson
       fields = ['id','phone', 'email']