class Terminal:

    def __init__(self, number=1, max_flights=20):
        self.number = number
        self.max_flights = max_flights
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)
        return self.flights

    def __str__(self):
        return "Terminal number {}".format(self.number)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def get_terminal_flights(self):
        return [el for el in self.flights]

    def get_terminal_flights_on(self, date):
        return [el for el in self.flights if el.start_time == date]

    def get_flights_for(self, date):
        return len(self.flights)

    def get_flights_before(self, date, hour):
        return [el for el in self.flights
                if (el.start_time.day, el.start_time.month,
                    el.start_time.year) ==
                (date.day, date.month, date.year) and
                el.start_time.hour < hour]

    def get_flight_from(self, destination):
        return [el for el in self.flights if el.from_dest == destination]

    def get_flight_to(self, destination):
        return [el for el in self.flights if el.to_dest == destination]

    def get_flight_to_hour(self, destination, date, hour):
        return [el for el in self.flights if el.to_dest == destination and
                el.start_time == date and el.start_time.hour == hour]

    def get_flight_from_hour(self, destination, date, hour):
        return [el for el in self.flights if el.from_dest == destination and
                el.start_time == date and el.start_time.hour == hour]

    def terminal_flights_to_dest(self, destination):
        return [el for el in self.flights if el.to_dest == destination]

    def flights_on_date_lt_hours(self, date, hours):
        return [el for el in self.flights if el.start_time == date and
                el.flight_duration() < hours]


def main():
    pass


if __name__ == "__main__":
    main()
