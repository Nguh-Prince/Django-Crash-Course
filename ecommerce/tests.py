from django.test import TestCase
from django.core.exceptions import ValidationError

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