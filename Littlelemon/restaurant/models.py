from django.db import models

# Create your models here.
class BookingModel(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=6)
    bookingDate = models.DateTimeField()

    def get_booking(self):
        return f'{self.name}-{self.no_of_guests}'

class MenuModel(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=5)

    def get_menu(self):
        return f'{self.title}: {str(self.price)}'