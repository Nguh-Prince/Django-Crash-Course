from django.db import models

class Collection(models.Model):
    name = models.CharField(max_length=20, unique=True)
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Collection"
        verbose_name_plural = "Collections"
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    description = models.TextField(blank=True, null=True)
    cover_image = models.FileField(null=True)
    quantity = models.IntegerField(default=0)

    # validate the price and quantity using the clean method and write a test

class CollectionProduct(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    # validate product and variant name are unique together

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file = models.FileField()

class Order(models.Model):
    time_made = models.DateTimeField(auto_now_add=True)
    discount = models.FloatField(default=0) # given in fractions, from 0 - 1

    # create a method for getting the total order price
    # validate the discount > 0 and < 1

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    # validate quantity > 0