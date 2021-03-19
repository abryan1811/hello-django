from django.test import TestCase
from .models import Item


class TestDjango(TestCase):

    def test_done_default_to_false(self):
        item = Item.objects.create(name="TEST TODO ITEM")
        self.assertFalse(item.done)
