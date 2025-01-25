from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer


# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class DeactivateOrderView(APIView):
    def patch(self, request, *args, **kwargs):
        try:
            order = Order.objects.get(id=kwargs["id"])
        except Order.DoesNotExist:
            return Response({"message": "Order not found"}, status=404)
        order.is_active = False
        order.save()

        return Response({"message": "Order deactivated"}, status=200)
