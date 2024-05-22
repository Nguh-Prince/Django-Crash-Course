from django.contrib import admin

from .models import *

class ImageInline(admin.StackedInline):
    model = Image
    extra = 3

class VariantInline(admin.StackedInline):
    model = Variant
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, VariantInline]

admin.site.register(Collection)
admin.site.register(Product, ProductAdmin)
admin.site.register(CollectionProduct)
admin.site.register(Order)
admin.site.register(OrderProduct)
