from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from .models import *

class ProductModelTests(TestCase):
    def test_price_less_than_0_raises_error(self):
        """
        checks whether the save method raises a ValidationError when the price < 0
        """
        product = Product(name='Test product', quantity=3, price=-950)

        self.assertRaises( ValidationError, product.save )

    def test_quantity_less_than_0_raises_error(self):
        """
        checks whether the save method raises a ValidationError when the quantity < 0
        """
        product = Product(name='Test product', quantity=-3, price=950)

        self.assertRaises( ValidationError, product.save )
    
    def test_quantity_and_price_less_than_0_raises_error(self):
        """
        checks whether the save method raises a ValidationError when the quantity < 0 and price < 0
        """
        product = Product(name='Test product', quantity=-3, price=-950)

        self.assertRaises( ValidationError, product.save )

class VariantModelTests(TestCase):
    def test_product_and_variant_name_unique_together(self):
        """
        Create and save a variant with a product and a name
        Create another variant with the same product and name as the first
        The save method of the second variant should raise a ValidationError
        """
        product = Product.objects.create(name='Test product', quantity=3, price=1000)
        v1 = Variant.objects.create(name='Testv', product=product)

        v2 = Variant(name='Testv', product=product)

        self.assertRaises( IntegrityError, v2.save )