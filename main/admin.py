from django.contrib import admin

from main.models import Car, Rental, Feedback, CarImage

# Register your models here.
admin.site.register(Car)
admin.site.register(Rental)
admin.site.register(Feedback)
admin.site.register(CarImage)


