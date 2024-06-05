from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from project.apps.contacts.models import ContactPerson
from project.apps.contacts.serializer import ContactPersonSerializer
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([AllowAny])
def contact_persons(request):
    if request.method == 'GET':
        data = ContactPerson.objects.all()
        serializer = ContactPersonSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
