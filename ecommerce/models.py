from typing import Iterable
from django.db import models
from django.core.exceptions import ValidationError

class Collection(models.Model):
    name = models.CharField(max_length=20, unique=True)
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Collection"
        verbose_name_plural = "Collections"

    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    description = models.TextField(blank=True, null=True)
    cover_image = models.FileField(null=True)
    quantity = models.IntegerField(default=0)
    time_created = models.DateTimeField(auto_now_add=True)

    # validate the price and quantity using the clean method and write a test
    def clean(self) -> None:
        if self.quantity < 0:
            raise ValidationError("The quantity of the product cannot be less than 0")
        if self.price < 0:
            raise ValidationError("The price of the product cannot be less than 0")
        
        return super().clean()

    def save(self, *args, **kwargs) -> None:
        self.clean()
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.name}: {self.price} XAF"
    
class CollectionProduct(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    # validate product and variant name are unique together
    class Meta:
        unique_together = [
            ["product", "name"]
        ]

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file = models.FileField()

class Order(models.Model):
    time_made = models.DateTimeField(auto_now_add=True)
    discount = models.FloatField(default=0) # given in fractions, from 0 - 1

    # create a method for getting the total order price
    # validate the discount >= 0 and <= 1

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    # validate quantity > 0

class CustomerFeedback(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.name[:10]}: {self.message[:20]}"
    
    @property
    def short_message(self) -> str:
        return self.message[:20]