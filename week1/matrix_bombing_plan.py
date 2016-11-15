from copy import deepcopy


def matrix_bombing_plan(m):
    res = {}

    for row in range(len(m)):
        for col in range(len(m[row])):
            res[(row, col)] = bomb_neighbours((row, col), deepcopy(m))

    return res


def sum_matrix(m):
    return sum(el for row in m for el in row)


def validate_neighbours(pos, n, m):
    if pos[0] < 0 or pos[0] >= n or pos[1] < 0 or pos[1] >= m:
        return False
    else:
        return True


def bomb_neighbours(el, m):

    for i in range(-1, 2):
        for j in range(-1, 2):
            if validate_neighbours((el[0] + i, el[1] + j), len(m), len(m[0])) \
               and (el[0] + i, el[1] + j) != el:
                target = m[el[0] + i][el[1] + j] - m[el[0]][el[1]]
                m[el[0] + i][el[1] + j] = max(0, target)

    return sum_matrix(m)
