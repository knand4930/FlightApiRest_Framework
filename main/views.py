from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponse
from .models import Flights,  Passenger, Reservation
from .serializers import FlightsSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def find_flights(request):
    flights = Flights.objects.filter(departureCity=request.data['departureCity'], arrivalCity=request.data['arrivalCity'], dateofDeparture=request.data['dateofDeparture'])
    serializer = FlightsSerializer(flights, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def save_reservation(request):
    flight = Flights.objects.get(id=request.data['flightId'])

    passenger = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.lastName = request.data['lastName']
    passenger.middleName = request.data['middleName']
    passenger.phone = request.data['phone']
    passenger.email = request.data['email']
    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger
    reservation.save()

    return Response(status=status.HTTP_201_CREATED)

class FlightViewSets(viewsets.ModelViewSet):
    queryset = Flights.objects.all()
    serializer_class = FlightsSerializer

class PassengerViewSets(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class ReservationViewSets(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer