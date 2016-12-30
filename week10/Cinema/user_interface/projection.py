class Projection:

    def __init__(self):
        self.hall = [['.' for x in range(10)] for y in range(10)]

    def __str__(self):
        return "Here be a hall:\n {} ".format(self.hall)

    def __repr__(self):
        return self.__str__()


def main():
    proj = Projection()
    print(proj)


if __name__ == '__main__':
    main()
