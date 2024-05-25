from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def index(request):
    recent_products = Product.objects.order_by("-time_created")[:5]

    return render(request, template_name="ecommerce/index.html", context={
        "new_arrivals": recent_products
    })

def collections(request, collection_id=None):
    collections = Collection.objects.all() 

    if not collection_id:
        # get all the unique products whose collectionproducts' collections 
        # are in the `collections` list
        products = Product.objects.filter(
            collectionproduct__collection__in=collections
        ).distinct()
        print(f'Query is {products.query}')
    else:
        # get all the unique products whose collectionproducts' collections
        # have id `collection_id`
        products = Product.objects.filter(
            collectionproduct__collection__id=collection_id
        ).distinct()
        print(f'Query is {products.query}')

    return render(request, template_name='ecommerce/collections.html', context={
        "collections": collections,
        "products": products,
        # "collection_id": collection_id,
        "collection": collections.filter(id=collection_id).first()
    })
