from django.db import models

# Create your models here.

class Flights(models.Model):
    flightNumber = models.CharField(max_length=10)
    OperatingAirlines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20)
    arrivalCity = models.CharField(max_length=20)
    dateofDeparture = models.DateField()
    estimatedTimeofDeparture = models.TimeField()
    
    def __str__(self):
        return self.flightNumber + ' '+ self.departureCity + ' To ' + self.arrivalCity

class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=20)

    def __str__(self):
        return self.firstName + ' ' + self.middleName + ' ' + self.lastName

class Reservation(models.Model):
    flight = models.ForeignKey(Flights,  on_delete=models.CASCADE, null=True)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE, null=True)

