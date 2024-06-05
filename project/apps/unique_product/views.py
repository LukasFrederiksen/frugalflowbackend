from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from project.apps.product.models import Product
from project.apps.unique_product.models import UniqueProduct
from project.apps.unique_product.serializer import UniqueProductSerializer
from django.db.models import Q, F
from rest_framework.pagination import PageNumberPagination

# Create your views here.
@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def unique_products(request):
    if request.method == 'POST':
        serializer = UniqueProductSerializer(data=request.data)
        if serializer.is_valid():
            product_id = request.data['product_id']
            try:
                Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({'error': 'Parent product does not exist'})
            serializer.save()
            return Response({"message": "UniqueProduct created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        search = request.GET.get('search')
        isDeleted = request.GET.get('isDeleted')
        show_all = request.GET.get('show_all', 'false').lower() == 'true'

        found_products = UniqueProduct.objects.all()

        if isDeleted == 'true':
            found_products = found_products.filter(isDeleted=False)
        elif isDeleted == 'false':
            found_products = found_products.filter(isDeleted=True)

        found_products = found_products.order_by(F('serial_number'))

        if search:
            found_products = found_products.filter(Q(serial_number__icontains=search) |
                                                   Q(product__name__icontains=search) |
                                                   (Q(case__isnull=False) & Q(case__vessel__icontains=search)))

        if show_all:
            serializer = UniqueProductSerializer(found_products, many=True)
            return Response(serializer.data)
        else:
            paginator = PageNumberPagination()
            paginator.page_size = 20
            paginated_products = paginator.paginate_queryset(found_products, request)
            serializer = UniqueProductSerializer(paginated_products, many=True)
            return paginator.get_paginated_response(serializer.data)
