from date import Date
from terminal import Terminal
from datetime import datetime


class Flight:

    def __init__(self, start_time=Date(29, 11, 2016, '12:31'),
                 end_time=Date(29, 11, 2016, '15:30'),
                 passengers=100, max_passengers=120,
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


def main():
    pass


if __name__ == "__main__":
    main()
