import unittest
from terminal import Terminal
from flight import Flight, Passenger, Reservation
from date import Date


class TestTerminal(unittest.TestCase):

    def setUp(self):
        self.terminal = Terminal()
        self.flight = Flight()
        self.flight2 = Flight(start_time=Date(day=29,
                              month=11, year=2016, hour='17:30'),
                              from_dest="Vancouver", to_dest="New York",
                              end_time=Date(day=29, month=11,
                              year=2016, hour='20:40'))
        self.terminal.add_flight(self.flight)
        self.terminal.add_flight(self.flight2)

    def test_init(self):
        self.assertEqual(self.terminal.number, 1)
        self.assertEqual(self.terminal.max_flights, 20)

    def test_add_flight(self):
        flight = Flight()
        self.assertEqual(self.terminal.add_flight(flight),
                         [self.flight, self.flight2, flight])

    def test_str(self):
        self.assertEqual(str(self.terminal), "Terminal number 1")

    def test_get_terminal_flights_on(self):
        date = Date()
        self.assertEqual(self.terminal.get_terminal_flights_on(date),
                         self.terminal.flights)

    def test_get_terminal_flights(self):
        self.assertEqual(self.terminal.get_terminal_flights(),
                         self.terminal.flights)

    def test_terminal_flights_to_dest(self):
        destination = "London"
        self.assertEqual(self.terminal.terminal_flights_to_dest(destination),
                         [self.flight])

    def test_get_flights_for(self):  # passed
        date = Date()
        self.assertEqual(self.terminal.get_flights_for(date), 2)

    def test_get_flights_before(self):
        date = Date()
        hour = '16:30'
        self.assertEqual(self.terminal.get_flights_before(date, hour),
                         [self.flight])

    def test_get_flight_from(self):
        destination = self.flight.from_dest
        self.assertEqual(self.terminal.get_flight_from(destination),
                         [self.flight])

    def test_get_flight_to(self):
        destination = self.flight.to_dest
        self.assertEqual(self.terminal.get_flight_to(destination),
                         [self.flight])

    def test_get_flight_to_hour(self):
        destination = self.flight.to_dest
        date = Date()
        hour = '12:31'
        self.assertEqual(self.terminal.
                         get_flight_to_hour(destination, date, hour),
                         [self.flight])

    def test_get_flight_from_hour(self):
        destination = self.flight.from_dest
        date = Date()
        hour = '12:31'
        self.assertEqual(self.terminal.
                         get_flight_from_hour(destination, date, hour),
                         [self.flight])

    def test_flights_on_date_lt_hours(self):
        hours = 3.0
        date = Date()
        self.assertEqual(self.terminal.flights_on_date_lt_hours(date, hours),
                         [self.flight])

    def test_flights_within_duration(self):
        start_time = Date(day=29, month=11, year=2016, hour='17:30')
        end_time = Date(day=29, month=11, year=2016, hour='20:40')
        self.assertEqual(self.terminal.flights_within_duration(start_time,
                                                               end_time),
                         [self.flight2])

    def test_passengers_to_dest(self):
        destination = self.flight.to_dest
        passenger = Passenger(first_name="Georgi", second_name="Atanasov",
                              age=20, flight=self.flight)
        passenger2 = Passenger(flight=self.flight2)
        self.flight.add_passenger(passenger)
        self.flight2.add_passenger(passenger2)
        self.assertEqual(self.terminal.passengers_to_dest(destination),
                         [passenger])

    def test_flights_with_passengers_gt(self):
        size = 0
        passenger = Passenger(first_name="Georgi", second_name="Atanasov",
                              age=20, flight=self.flight)
        passenger2 = Passenger(flight=self.flight2)
        self.flight.add_passenger(passenger)
        self.flight2.add_passenger(passenger2)
        self.assertEqual(self.terminal.flights_with_passengers_gt(size),
                         [self.flight, self.flight2])

    def test_reservations_to_destination(destination):
        destination = "London"
        pass


if __name__ == '__main__':
    unittest.main()
