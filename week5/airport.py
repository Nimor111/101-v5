from flight import Flight
from date import Date


class Airport:

    def __init__(self, name="Sofia"):
        self.name = name
        self.terminals = []
        self.flights = [Flight(), Flight(start_time=Date(day=29,
                                         month=11, year=2016, hour='17:30'),
                                         from_dest="Vancouver",
                                         to_dest="New York")]

    def add_terminal(self, terminal):
        self.terminals.append(terminal)
        return self.terminals


def main():
    pass


if __name__ == "__main__":
    main()
