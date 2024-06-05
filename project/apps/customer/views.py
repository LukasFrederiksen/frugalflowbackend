from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from project.apps.customer.models import Customer
from project.apps.customer.serializer import CustomerSerializer
from rest_framework.response import Response


# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def customers(request):
    if request.method == 'GET':
        show_all = request.GET.get('show_all', 'false').lower() == 'true'  # Will be True if 'show_all=true' is passed

        data = Customer.objects.all()

        if show_all:
            serializer = CustomerSerializer(data, many=True)
            return Response(serializer.data)
        else:
            serializer = CustomerSerializer(data, context={'request': request}, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'customer': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([AllowAny])
def customer(request, id):
    #  invoke serializer and return client
    try:
        data = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'customer': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def customer_count(request):
    try:
        query = Customer.objects.all()

        count = query.count()

        return Response({"count": count}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
