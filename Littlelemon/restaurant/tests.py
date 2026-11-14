from django.test import TestCase

from .models import BookingModel, MenuModel

from datetime import datetime

# Create your tests here.

class ModelTest(TestCase):
    def test_get_menu(self):
        menu = MenuModel.objects.create(title='Lemon Desert', price=10.2, inventory=100)
        self.assertEqual(menu.get_menu(), 'Lemon Desert: 10.2')

    def test_get_booking(self):
        booking = BookingModel.objects.create(name='Bonwi', no_of_guests=3, bookingDate=datetime.now())
        self.assertEqual(booking.get_booking(), 'Bonwi-3')

