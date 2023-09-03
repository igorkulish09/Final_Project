from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class APIResponseView(APIView):
    def get(self, request):
        data = {"message": "Hello, API!"}
        return Response(data)
