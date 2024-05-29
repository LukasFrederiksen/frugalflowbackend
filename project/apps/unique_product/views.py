from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([AllowAny])
def unique_products(request):
    try:
        p1 = {'id': 21, 'name': 'Torquemeter', 'serial_number': 919191, 'status_shipping': 'Shipped', 'status_payment': 'Paid', 'vessel': 'Tina Theresa'}
        p2 = {'id': 22, 'name': 'Flowmeter', 'serial_number': 123123, 'status_shipping': 'Arrived', 'status_payment': 'Awaiting Payment', 'vessel': 'Tina Theresa'}
        p3 = {'id': 23, 'name': 'PLS', 'serial_number': 887788, 'status_shipping': 'Not Sent', 'status_payment': 'Invoice Sent', 'vessel': 'Mona Swan'}

        unique_products = [p1,p2,p3]



        return Response(unique_products, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

