def transpose(m):
    transposed = []
    for i in range(len(m[0])):
        transposed.append([0] * len(m))

    for i in range(len(m)):
        for j in range(len(m[i])):
            transposed[j][i] = m[i][j]

    return transposed


def check_threes(row, col, m):
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    idx_m1 = 0
    idx_m2 = 0
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            matrix[idx_m1][idx_m2] = m[i][j]
            idx_m2 += 1
        idx_m1 += 1
        idx_m2 = 0
    flattened = sorted([val for sublist in matrix for val in sublist])

    return flattened == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def sudoku_solved(sudoku):
    list_to_check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for el in sudoku:
        if sorted(el) != list_to_check:
            return False
    for el in transpose(sudoku):
        if sorted(el) != list_to_check:
            return False

    for row in range(6, 3):
        for col in range(6, 3):
            if check_threes(row, col, sudoku) is False:
                return False
    return True


def main():
    # True
    print(sudoku_solved([
        [4, 5, 2, 3, 8, 9, 7, 1, 6],
        [3, 8, 7, 4, 6, 1, 2, 9, 5],
        [6, 1, 9, 2, 5, 7, 3, 4, 8],
        [9, 3, 5, 1, 2, 6, 8, 7, 4],
        [7, 6, 4, 9, 3, 8, 5, 2, 1],
        [1, 2, 8, 5, 7, 4, 6, 3, 9],
        [5, 7, 1, 8, 9, 2, 4, 6, 3],
        [8, 9, 6, 7, 4, 3, 1, 5, 2],
        [2, 4, 3, 6, 1, 5, 9, 8, 7]
    ]))
    # False
    print(sudoku_solved([
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]))


if __name__ == "__main__":
    main()
