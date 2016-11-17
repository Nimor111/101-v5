# from flight import Flight
# from date import Date


class Airport:

    def __init__(self, name="Sofia"):
        self.name = name
        self.terminals = []

    def add_terminal(self, terminal):
        self.terminals.append(terminal)
        return self.terminals

    def passengers_from_terminal(self, terminal):
        passengers = []
        for flight in terminal.flights:
            for passenger in flight.psgrs:
                passengers.append(passenger)

        return passengers


def main():
    pass


if __name__ == "__main__":
    main()
