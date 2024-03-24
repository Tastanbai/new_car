from django.db import models

# Create your models here.
class Car(models.Model):
    image=models.ImageField(upload_to='car_images',null=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_type = models.CharField(max_length=50)
    volume = models.DecimalField(max_digits=5, decimal_places=2)
    is_rented = models.BooleanField(default=False)

def __str__(self):
    return self.name

class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    agent = models.CharField(max_length=100)
    date_out = models.DateField()
    time_out = models.TimeField()
    date_in = models.DateField()
    time_in = models.TimeField()
    fuel = models.DecimalField(max_digits=5, decimal_places=2)
    mileage = models.PositiveIntegerField()
    payment = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField()

    def __str__(self):
        return f"Rental of {self.car.name} by {self.agent}"


class Feedback(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return f"Feedback from {self.first_name} {self.last_name}"
