import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from django.db.models import Q

from project.apps.case.models import Case
from project.apps.case.serializer import CaseSerializer

from project.apps.kafka.kafka_client import KafkaProducer
from project.apps.product.serializer import ProductSerializer




@api_view(['GET', 'POST'])
def cases(request):
    if request.method == 'GET':
        # Henter parameter fra vores request
        search = request.GET.get('search')
        sortprice = request.GET.get('sortprice')
        sortdeadline = request.GET.get('sortdeadline')

        # PageNumberPagination som håndterer pagineringen
        paginator = PageNumberPagination()
        paginator.page_size = 20

        # Vores forspøgelse, henter alle cases
        found_cases = Case.objects.all().select_related('customer')

        # Anvend søgefilter, hvis 'søgning' parameteren er angivet
        if search:
            found_cases = found_cases.filter(Q(title__icontains=search) | Q(description__icontains=search))

        # sorting price
        if sortprice == 'asc':
            found_cases = found_cases.order_by('total_price')
        elif sortprice == 'desc':
            found_cases = found_cases.order_by('-total_price')

        # sorting deadline
        if sortdeadline == 'asc':
            found_cases = found_cases.order_by('deadline')
        elif sortdeadline == 'desc':
            found_cases = found_cases.order_by('-deadline')

        # Paginer forespørgslen ved hjælp af paginator
        paginated_cases = paginator.paginate_queryset(found_cases, request)

        # Serializer paginerede forespørgslen
        serializer = CaseSerializer(paginated_cases, many=True)

        # Return pagineret response
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = CaseSerializer(data=request.data)
        if serializer.is_valid():
            producer = KafkaProducer()

            try:
                serializer.save()

                case_data = serializer.data
                case_data['priority'] = 10

                data = json.dumps(case_data)
                producer.send('case_created', data)
                return Response({'case': serializer.data}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            finally:
                producer.close()

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def case(request, id):
    try:
        case = Case.objects.get(id=id)
    except Case.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CaseSerializer(case)
        return Response(serializer.data)

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


@api_view(['POST'])
def add_product(request):
    try:
        is_unique = request.data['is_unique']
        serializer = None
        if is_unique == 0:
            serializer = CaseSimpleProductSerializer(data=request.data)
        elif is_unique == 1:
            serializer = CaseUniqueProductSerializer(data=request)
        if serializer.is_valid():
            serializer.save()
            return Response({'Product': serializer.data}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response("Error adding Product", status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
