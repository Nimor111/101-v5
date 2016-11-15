import unittest
from airport import Airport
from date import Date
from flight import Flight
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


if __name__ == "__main__":
    unittest.main()
