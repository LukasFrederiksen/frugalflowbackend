import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from django.db.models import Q

from project.apps.case.models import Case
from project.apps.case.serializer import CaseSerializer

from project.apps.kafka.kafka_client import KafkaProducer
from project.apps.unique_product.serializer import UniqueProductSerializer


@api_view(['GET', 'POST'])
def cases(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        sortdeadline = request.GET.get('sortdeadline')

        paginator = PageNumberPagination()
        paginator.page_size = 20

        found_cases = Case.objects.all()
        if search:
            found_cases = found_cases.filter(Q(title__icontains=search) | Q(description__icontains=search))

        if sortdeadline == 'asc':
            found_cases = found_cases.order_by('deadline')
        elif sortdeadline == 'desc':
            found_cases = found_cases.order_by('-deadline')

        paginated_cases = paginator.paginate_queryset(found_cases, request)

        serializer = CaseSerializer(paginated_cases, many=True)

        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = CaseSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'case': serializer.data}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def case(request, id):
    try:
        case = Case.objects.get(id=id)
    except Case.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        unique_products = case.unique_products.all()
        ups = UniqueProductSerializer(unique_products, many=True)
        serializer = CaseSerializer(case)
        return Response({'case': serializer.data, 'unique_products': ups.data}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = CaseSerializer(case, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        case.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def case_count(request):
    try:
        case_status = request.GET.get('case_status')

        if case_status:
            query = Case.objects.filter(case_status=case_status)
        else:
            query = Case.objects.all()

        count = query.count()

        return Response({"count": count}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
