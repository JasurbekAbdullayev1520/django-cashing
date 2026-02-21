from django.db import models


class Category(models.Model):
    name = models.CharField()
    description = models.TextField()


class Product(models.Model):
    name = models.CharField()
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    
