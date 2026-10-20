from rest_framework import serializers
from .models import Customer, Transaction
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "id",
            "name",
            "email",
            "created_at"
        ]
        read_only_fields = ["id", "created_at"]

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "customer",
            "amount",
            "merchant",
            "country",
            "timestamp",
            "risk_score",
            "flagged",
        ]
        read_only_fields = [
            "id",
            "timestamp",
            "risk_score",
            "flagged"
        ]