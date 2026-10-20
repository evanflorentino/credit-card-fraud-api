from django.urls import path
from .views import CustomerListCreateView, TransactionListCreateView

urlpatterns = [
    path("customers/", CustomerListCreateView.as_view(), name="customer-list"),
    path("transactions/", TransactionListCreateView.as_view(),name="transaction-list"),
]