from functools import reduce


ALIVE = 1
DEAD = 0


def strawberries(rows, columns, days, dead_strawberries):
    if rows < 1 and rows > 1000:
        raise ValueError("Invalid number of rows")
    if columns < 1:
        raise ValueError("Invalid number of cols")
    if rows > columns:
        raise ValueError("Rows cannot be greater than columns")
    field = [[ALIVE for i in range(columns)] for j in range(rows)]

    for strawberry in dead_strawberries:
        field[strawberry[0]][strawberry[1]] = DEAD

    for day in range(days):
        for el in dead_strawberries:
                    if validator((el[0] - 1, el[1]), (rows, columns)):
                        field[el[0] - 1][el[1]] = DEAD
                    if validator((el[0], el[1] - 1), (rows, columns)):
                        field[el[0]][el[1] - 1] = DEAD
                    if validator((el[0], el[1] + 1), (rows, columns)):
                        field[el[0]][el[1] + 1] = DEAD
                    if validator((el[0] + 1, el[1]), (rows, columns)):
                        field[el[0] + 1][el[1]] = DEAD
        dead_strawberries = [(row, col) for row in range(rows)
                             for col in range(columns)
                             if field[row][col] == DEAD]

    return sum(reduce(lambda x, y: x + y, field))


def validator(idx, length):
    return bool(idx[0] >= 0 and idx[0] < length[0] and
                idx[1] >= 0 and idx[1] < length[1])


def has_dead_neighbours(idx, length, matrix):
    return bool(idx[0] >= 0 and idx[0] < length[0] and
                idx[1] >= 0 and idx[1] < length[1]) and \
        bool(idx[0] >= 0 and idx[0] < length[0] and
             idx[1] >= 0 and idx[1] < length[1]) and \
        bool(idx[0] >= 0 and idx[0] < length[0] and
             idx[1] >= 0 and idx[1] < length[1]) and \
        bool(idx[0] >= 0 and idx[0] < length[0] and
             idx[1] >= 0 and idx[1] < length[1])


def main():
    print(strawberries(400, 803, 99, [(399, 200), (196, 202)]))
    print(strawberries(8, 10, 2, [(4, 8), (2, 7)]))


if __name__ == '__main__':
    main()
