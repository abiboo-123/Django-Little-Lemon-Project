from django.test import TestCase  
from .models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        # Create a MenuItem object
        item = MenuItem.objects.create(Title="IceCream", Price=80, Inventory=100)
        
        # Check if the string representation (__str__) is correct
        self.assertEqual(str(item), 'IceCream : 80')
