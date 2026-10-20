from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="transactions"
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    merchant = models.CharField(max_length=150)
    country = models.CharField(max_length=100)
    timestap = models.DateTimeField(auto_now_add=True)

    #fraud detection
    risk_score = models.FloatField(default=0.0)
    flagged = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer.name} - ${self.amount}"
