from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from django.db.models import Q

from project.apps.manufacture.models import Manufacture
from project.apps.manufacture.serializer import ManufactureSerializer


@api_view(['GET', 'POST'])
def manufactures(request):
    if request.method == 'GET':
        # Henter parameter fra vores request
        search = request.GET.get('search')
        sortname = request.GET.get('sortname')
        is_deleted = request.GET.get('isdeleted')

        # PageNumberPagination som håndterer pagineringen
        paginator = PageNumberPagination()
        paginator.page_size = 20

        # Vores forespørgelse, henter alle manufactures
        found_manufactures = Manufacture.objects.all()

        # Anvend søgefilter, hvis 'søgning' parameteren er angivet
        if search:
            found_manufactures = found_manufactures.filter(Q(name__icontains=search))

        # Sorting name
        if sortname == 'asc':
            found_manufactures = found_manufactures.order_by('name')
        elif sortname == 'desc':
            found_manufactures = found_manufactures.order_by('-name')

        # Tjekker om manufacturen er deleted eller ej
        if is_deleted == 'true':
            found_manufactures = found_manufactures.filter(isdeleted=True)
        elif is_deleted == 'false':
            found_manufactures = found_manufactures.filter(isdeleted=False)

        # Paginer forespørgslen ved hjælp af paginator
        paginated_manufactures = paginator.paginate_queryset(found_manufactures, request)

        # Serializer paginerede forespørgslen
        serializer = ManufactureSerializer(paginated_manufactures, many=True)

        # Return pagineret response
        return paginator.get_paginated_response(serializer.data)


    elif request.method == 'POST':
        email = request.data.get('email', '')
        cvr = request.data.get('cvr', '')
        phone = request.data.get('phone', '')

        if email and Manufacture.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        if cvr and Manufacture.objects.filter(cvr=cvr).exists():
            return Response({'error': 'CVR already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        if phone and Manufacture.objects.filter(phone=phone).exists():
            return Response({'error': 'Phone Nr already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ManufactureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'manufactures': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def manufacture(request, id=None):
    if request.method == 'POST':
        serializer = ManufactureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'manufacture': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        data = Manufacture.objects.get(pk=id)
    except Manufacture.DoesNotExist:
        return Response({'error': 'Manufacturer not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ManufactureSerializer(data)
        return Response({'manufacture': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        email = request.data.get('email', '')
        cvr = request.data.get('cvr', '')
        phone = request.data.get('phone', '')

        try:
            serializer = ManufactureSerializer(data, data=request.data)
        except Manufacture.DoesNotExist:
            return Response({'error': 'Manufacturer does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if email and Manufacture.objects.filter(email=email).exclude(id=data.id).exists():
            return Response({'error': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        if cvr and Manufacture.objects.filter(cvr=cvr).exclude(id=data.id).exists():
            return Response({'error': 'CVR already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        if phone and Manufacture.objects.filter(phone=phone).exclude(id=data.id).exists():
            return Response({'error': 'Phone Nr already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response({'manufacture': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
