from date import Date
from terminal import Terminal
from datetime import datetime


class Flight:

    def __init__(self, start_time=Date(29, 11, 2016, '12:31'),
                 end_time=Date(29, 11, 2016, '15:30'),
                 passengers=0, max_passengers=120,
                 from_dest="Sofia", to_dest="London",
                 terminal=Terminal(2, 30), declined=False):
        self.start_time = start_time
        self.end_time = end_time
        self.passengers = passengers
        self.max_passengers = max_passengers
        self.from_dest = from_dest
        self.to_dest = to_dest
        self.terminal = terminal
        self.declined = declined
        self.psgrs = []
        self.reservations = []

    def __str__(self):
        return "Flight from {} to {} on {}".format(self.from_dest,
                                                   self.to_dest,
                                                   self.start_time)

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __repr__(self):
        return self.__str__()

    def flight_duration(self):
        return (datetime.strptime(self.end_time.hour, '%H:%M') -
                datetime.strptime(self.start_time.hour, '%H:%M')). \
            total_seconds() / 3600

    def add_passenger(self, passenger):
        if isinstance(passenger, Passenger) is False:
            raise TypeError("Must be a passenger!")
        reservation = Reservation(flight=self,
                                  passenger=passenger,
                                  accepted=True)
        self.reservations.append(reservation)
        self.psgrs.append(passenger)
        self.passengers += 1
        return self.psgrs

    def passengers_under_18(self, flight):
        return [psgr for psgr in self.psgrs if psgr.age < 18]

    def passenger_reservations(self):
        return [reservation for reservation in self.reservations]

    def flight_empty_seats(self):
        return self.max_passengers - self.passengers > 0


class Passenger:

    def __init__(self, first_name="Peter", second_name="Peshov",
                 flight=Flight(), age=22):
        self.first_name = first_name
        self.second_name = second_name
        self.flight = flight
        self.age = age

    def __str__(self):
        return "Name: {} {}, Age: {}, Flight: {}".format(self.first_name,
                                                         self.second_name,
                                                         self.age,
                                                         self.flight)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__str__() == other.__str__()


class Reservation:

    def __init__(self, flight=Flight(), passenger=Passenger(), accepted=True):
        self.flight = flight
        self.passenger = passenger
        self.accepted = accepted

    def __str__(self):
        return "Reservation for {} by passenger {}".format(self.flight,
                                                           self.passenger)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__str__() == other.__str__()


def main():
    pass


if __name__ == '__main__':
    main()
