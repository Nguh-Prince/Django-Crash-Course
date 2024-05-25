from django.urls import path

from . import views

app_name = 'ecommerce'

urlpatterns = [
    path('', views.index, name='index'),
    path('collections/', views.collections, name='collections'),
    path('collections/<int:collection_id>', views.collections, name='collections')
]