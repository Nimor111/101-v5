class Date:

    def __init__(self, day=29, month=11, year=2016, hour='15:30'):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour

    def __lt__(self, other):
        return self.hour < other.hour

    def __str__(self):
        return "{}/{}/{}".format(self.day, self.month, self.year)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__str__() == other.__str__()


def main():
    pass


if __name__ == "__main__":
    main()
