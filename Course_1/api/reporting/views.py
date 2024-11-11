from rest_framework import viewsets

from reporting.serializers import OrderSerializer
from reporting.models import Order

    

class OrderViewSet(viewsets.ModelViewSet):

    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return Order.objects.all().order_by('-created_time')
