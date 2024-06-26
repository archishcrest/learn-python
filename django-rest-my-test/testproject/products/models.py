from django.db import models
from customers.models import Customer

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(Customer, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
