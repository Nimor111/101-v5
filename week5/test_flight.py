import unittest
from flight import Flight
from date import Date
from terminal import Terminal
from datetime import datetime


class TestFlight(unittest.TestCase):

    def setUp(self):
        self.flight = Flight()

    def test_init(self):
        self.assertEqual(self.flight.start_time, Date(29, 11, 2016, '12:20'))
        self.assertEqual(self.flight.end_time, Date(29, 11, 2016, '15:30'))
        self.assertEqual(self.flight.passengers, 100)
        self.assertEqual(self.flight.max_passengers, 120)
        self.assertEqual(self.flight.from_dest, "Sofia")
        self.assertEqual(self.flight.to_dest, "London")
        self.assertEqual(self.flight.terminal, Terminal(2, 30))
        self.assertEqual(self.flight.declined, False)

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


if __name__ == "__main__":
    unittest.main()
