from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from project.apps.case.models import Case
from project.apps.case.serializer import CaseSerializer
from project.apps.users.models import User
from project.apps.users.serializer import UserSerializer, CustomTokenObtainPairSerializer


# Custom login validater
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def users(request):
    if request.method == 'GET':
        show_all = request.GET.get('show_all', 'false').lower() == 'true'  # Will be True if 'show_all=true' is passed
        data = User.objects.all()

        if show_all:
            serializer = UserSerializer(data, many=True)
            return Response(serializer.data)
        else:
            serializer = UserSerializer(data, context={'request': request}, many=True)
            return Response({'users': serializer.data})

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def user_detail(request, pk):
    try:
        data = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(data)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = UserSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_200_OK)


#  Get all cases for a user
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def all_cases_for_a_user(request, userid):
    try:
        user = User.objects.get(pk=userid)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        cases_per_page = request.GET.get('page_size', 10)
        # Filter cases by user
        user_cases = Case.objects.filter(product_owner=user, case_status='open')

        # PageNumberPagination for handling pagination
        paginator = PageNumberPagination()
        try:
            paginator.page_size = int(cases_per_page)  # Convert to integer
        except ValueError:
            return Response({"error": "Invalid page_size value"}, status=status.HTTP_400_BAD_REQUEST)

        # Paginate the queryset
        paginated_cases = paginator.paginate_queryset(user_cases, request)

        # Serialize paginated queryset
        serializer = CaseSerializer(paginated_cases, many=True)

        # Return paginated response
        return paginator.get_paginated_response(serializer.data)
