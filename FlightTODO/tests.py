from django.test import TestCase
from .models import Flight

class FlightModelTest(TestCase):
    def test_flight_creation(self):
        flight = Flight.objects.create(
            origin="Moscow",
            origin_icao="UUEE",
            dest="Saint Petersburg",
            dest_icao="ULLI",
            completed=False
        )
        self.assertEqual(flight.origin, "Moscow")
        self.assertEqual(flight.dest, "Saint Petersburg")
        self.assertFalse(flight.completed)
