from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from project.apps.vessel.models import Vessel
from project.apps.vessel.serializer import VesselSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q, F


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def vessels(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        isActive = request.GET.get('isActive')
        show_all = request.GET.get('show_all', 'false').lower() == 'true'  # Will be True if 'show_all=true' is passed

        found_vessels = Vessel.objects.all()

        found_vessels = found_vessels.order_by(F('id').desc())

        if search:
            found_vessels = found_vessels.filter(Q(imo__icontains=search) |
                                                 Q(name__icontains=search))

        if isActive == 'true':
            found_vessels = found_vessels.filter(isDeleted=False)
        elif isActive == 'false':
            found_vessels = found_vessels.filter(isDeleted=True)

        if show_all:
            serializer = VesselSerializer(found_vessels, many=True)
            return Response(serializer.data)  # Just return all the data
        else:
            paginator = PageNumberPagination()
            paginator.page_size = 10
            paginated_vessels = paginator.paginate_queryset(found_vessels, request)
            serializer = VesselSerializer(paginated_vessels, many=True)
            return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        imo = request.data.get('imo', '')

        if imo and Vessel.objects.filter(imo=imo).exists():
            return Response({'error': 'imo already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = VesselSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'vessel': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def vessel(request, id):
    try:
        data = Vessel.objects.get(pk=id)
    except Vessel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VesselSerializer(data)
        return Response({'vessel': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = VesselSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'vessel': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        data.isDeleted = 'True'
        data.save()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def vessel_count(request):
    try:
        is_deleted = request.GET.get('is_deleted')
        query = Vessel.objects.all()

        if is_deleted is not None:
            if is_deleted.lower() == 'true':
                query = query.filter(isDeleted=True)
            elif is_deleted.lower() == 'false':
                query = query.filter(isDeleted=False)

        count = query.count()
        return Response({"count": count}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
