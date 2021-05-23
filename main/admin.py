from django.contrib import admin
from .models import Flights, Passenger,  Reservation

# Register your models here.
admin.site.register(Flights)
admin.site.register(Passenger)
admin.site.register(Reservation)
