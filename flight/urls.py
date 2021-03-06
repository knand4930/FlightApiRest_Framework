"""flight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,  include
from django.conf import settings
from django.conf.urls.static import static
from main import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('flights', views.FlightViewSets)
router.register('passengers', views.PassengerViewSets)
router.register('reservations', views.ReservationViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('flightServices/', include(router.urls)),
    path('flightServices/findFlight/', views.find_flights),
    path('flightServices/saveReservations/', views.save_reservation),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
