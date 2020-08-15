from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)

class Stock(models.Model):

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stock'

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=3)
    remarks = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):

        return self.name

