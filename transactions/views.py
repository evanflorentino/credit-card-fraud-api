from django.shortcuts import render
from rest_framework import generics

from .models import Customer, Transaction
from .serializers import CustomerSerializer, TransactionSerializer

# Create your views here.
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


