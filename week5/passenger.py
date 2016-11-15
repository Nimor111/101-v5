from flight import Flight


class Passenger:

    def __init__(self, first_name="Peter", second_name="Peshov",
                 flight=Flight(), age=22):
        self.first_name = first_name
        self.second_name = second_name
        self.flight = flight
        self.age = age


def main():
    pass


if __name__ == '__main__':
    main()
