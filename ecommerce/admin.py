from django.contrib import admin

from .models import *

admin.AdminSite

class ImageInline(admin.StackedInline):
    model = Image
    extra = 3

class VariantInline(admin.StackedInline):
    model = Variant
    extra = 3

class CollectionProductInline(admin.StackedInline):
    model = CollectionProduct
    extra = 3

class OrderProductInline(admin.StackedInline):
    model = OrderProduct
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, VariantInline, CollectionProductInline]
    list_display = ("name", "price", "quantity", "time_created")

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline]

class CustomerFeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'short_message', 'time_created')

admin.site.register(Collection)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(CustomerFeedback, CustomerFeedbackAdmin)
