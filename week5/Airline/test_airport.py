import unittest
from airport import Airport
from date import Date
from flight import Flight, Passenger
from terminal import Terminal


class TestAirport(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()
        self.flight = Flight()
        self.flight2 = Flight(start_time=Date(day=29,
                              month=11, year=2016, hour='17:30'),
                              from_dest="Vancouver", to_dest="New York")
        self.terminal = Terminal()
        self.airport.add_terminal(self.terminal)

    def test_init(self):  # passed
        self.assertEqual(self.airport.name, "Sofia")
        self.assertEqual(self.airport.terminals, [self.terminal])

    def test_add_terminal(self):
        self.assertEqual(self.airport.add_terminal(self.terminal),
                         [self.terminal, self.terminal])

    def test_passengers_from_terminal(self):
        passenger = Passenger(first_name="Georgi", second_name="Atanasov",
                              age=20, flight=self.flight)
        passenger2 = Passenger(flight=self.flight2)
        self.flight.add_passenger(passenger)
        self.flight2.add_passenger(passenger2)
        self.terminal.add_flight(self.flight)
        self.terminal.add_flight(self.flight2)
        self.assertEqual(self.airport.passengers_from_terminal(
            self.terminal),
            [passenger, passenger2])


if __name__ == "__main__":
    unittest.main()
