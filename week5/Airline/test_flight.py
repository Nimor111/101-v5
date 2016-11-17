import unittest
from date import Date
from terminal import Terminal
from datetime import datetime
from flight import Flight, Passenger, Reservation


class TestFlight(unittest.TestCase):

    def setUp(self):
        self.flight = Flight()
        self.flight2 = Flight(start_time=Date(day=29,
                              month=11, year=2016, hour='17:30'),
                              from_dest="Vancouver", to_dest="New York")

    def test_init(self):
        self.assertEqual(self.flight.start_time, Date(29, 11, 2016, '12:20'))
        self.assertEqual(self.flight.end_time, Date(29, 11, 2016, '15:30'))
        self.assertEqual(self.flight.passengers, 0)
        self.assertEqual(self.flight.max_passengers, 120)
        self.assertEqual(self.flight.from_dest, "Sofia")
        self.assertEqual(self.flight.to_dest, "London")
        self.assertEqual(self.flight.terminal, Terminal(2, 30))
        self.assertEqual(self.flight.declined, False)
        self.assertEqual(self.flight.psgrs, [])
        self.assertEqual(self.flight.reservations, [])

    def test_str(self):
        self.assertEqual(str(self.flight),
                         "Flight from Sofia to London on 29/11/2016")

    def test_flight_duration(self):
        self.assertEqual
        (self.flight.
            flight_duration(),
            (datetime.strptime(self.flight.end_time.hour, '%H:%M') -
             datetime.strptime(self.flight.start_time.hour, '%H:%M')).
            total_seconds() / 3600)

    def test_add_passenger(self):
        passenger = Passenger()
        self.assertEqual(self.flight.add_passenger(passenger), [passenger])

    def test_passengers_under_18(self):
        passenger = Passenger(age=16)
        self.flight.add_passenger(passenger)
        self.assertEqual(self.flight.passengers_under_18(self.flight),
                         [passenger])

    def test_passenger_reservations(self):
        passenger = Passenger(first_name="Georgi", second_name="Atanasov",
                              age=20, flight=self.flight)
        passenger2 = Passenger(flight=self.flight2)
        reservation = Reservation(passenger=passenger, flight=self.flight)
        reservation2 = Reservation(passenger=passenger2, flight=self.flight2)
        self.flight.add_passenger(passenger)
        self.flight2.add_passenger(passenger2)
        self.assertEqual(self.flight.passenger_reservations(),
                         [reservation])
        self.assertEqual(self.flight2.passenger_reservations(),
                         [reservation2])

    def test_flight_empty_seats(self):
        self.assertTrue(self.flight.flight_empty_seats())


if __name__ == "__main__":
    unittest.main()
