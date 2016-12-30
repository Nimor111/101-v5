import numpy as np


class Projection:

    def __init__(self):
        self.hall = np.array([["." for x in range(11)] for y in range(11)])
        number_row = ["-", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.hall[0] = number_row
        for row in range(1, 11):
            self.hall[row][0] = row - 1

    def __str__(self):
        return "Here be a hall:\n{}".format(self.__print_matrix())

    def __print_matrix(self):
        return ('\n'.join([''.join(['{:2}'.format(item) for item in row])
                for row in self.hall]))

    def __repr__(self):
        return self.__str__()

    def reserve_seat(self, row, col):
        if row == 0 or col == 0:
            raise IndexError
        self.hall[row][col] = 'x'
        return self.hall


def main():
    proj = Projection()
    proj.reserve_seat(1, 1)
    proj.reserve_seat(2, 2)
    print(proj)


if __name__ == '__main__':
    main()
