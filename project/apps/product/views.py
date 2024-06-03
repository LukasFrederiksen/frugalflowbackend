from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from project.apps.product.models import Product, UniqueProduct
from project.apps.product.serializer import ProductSerializer, SimpleProductSerializer, \
    UniqueProductSerializer
from rest_framework.response import Response
from django.db.models import Q, F


@api_view(['POST'])
@permission_classes([AllowAny])
def product_create(request):



    # Check if data for SimpleProduct is provided
    if 'is_unique' in request.data:
        if request.data['is_unique'] == 0:
            serializer = SimpleProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "SimpleProduct created successfully."}, status=status.HTTP_201_CREATED)
        else:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Product created successfully."}, status=status.HTTP_201_CREATED)
            serializer = SimpleProductSerializer(data=request.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Check if data for UniqueProduct is provided
    elif 'serial_number' in request.data:
        serializer = UniqueProductSerializer(data=request.data)
        if serializer.is_valid():
            product_id = request.data['product_id']
            try:
                Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({'error': 'Parent product does not exist'})
            serializer.validated_data["product_id"] = product_id
            serializer.save()
            return Response({"message": "UniqueProduct created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({"error": "Invalid data provided."}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def products(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        isDeleted = request.GET.get('isDeleted')
        show_all = request.GET.get('show_all', 'false').lower() == 'true'

        found_products = Product.objects.all()

        found_products = found_products.order_by(F('serial_number'))

        if search:
            found_products = found_products.filter(Q(sku__icontains=search) |
                                                   Q(serial_number__icontains=search) |
                                                   Q(name__icontains=search))

        if isDeleted == 'true':
            found_products = found_products.filter(isDeleted=False)
        elif isDeleted == 'false':
            found_products = found_products.filter(isDeleted=True)

        if show_all:
            serializer = ProductSerializer(found_products, many=True)
            return Response(serializer.data)
        else:
            paginator = PageNumberPagination()
            paginator.page_size = 20
            paginated_products = paginator.paginate_queryset(found_products, request)
            serializer = ProductSerializer(paginated_products, many=True)
            return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        sn = request.data.get('serial_number', '')
        if sn and Product.objects.filter(serial_number=sn).exists():
            return Response({'error': 'serial_number already exits.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Product': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def product(request, id):
    try:
        data = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(data)
        return Response({'product': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ProductSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'product': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        data.is_deleted = 'True'
        data.save()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def product_count(request):
    try:
        is_deleted = request.GET.get('is_deleted')
        location = request.GET.get('location')

        query = Product.objects.all()

        if is_deleted is not None:
            if is_deleted.lower() == 'true':
                query = query.filter(is_deleted=True)
            elif is_deleted.lower() == 'false':
                query = query.filter(is_deleted=False)

        if location is not None:
            query = query.filter(location=location)

        count = query.count()
        return Response({"count": count}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
