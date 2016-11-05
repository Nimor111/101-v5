import os
import numpy as np
import time

ALIVE = '■'
DEAD = '□'

number_of_cells = int(input("Insert number_of_cells: "))
game_matrix = [[DEAD for i in range(9)] for j in range(9)]
for i in range(number_of_cells):
    x, y = map(int, input().split())
    game_matrix[x - 1][y - 1] = ALIVE


def validate_coordinates(at):
    if at[0] < 0 or at[0] >= len(game_matrix):
        return False

    if at[1] < 0 or at[1] >= len(game_matrix[0]):
        return False

    return True


def check_neighbours(x, y):
    live_cells = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if validate_coordinates((x + i, y + j)):
                if game_matrix[x + i][y + j] == ALIVE:
                    live_cells += 1
    if game_matrix[x][y] == DEAD:
        if live_cells >= 3:
            game_matrix[x][y] = ALIVE
    else:
        if live_cells == 0 or live_cells == 1 or live_cells >= 4:
            game_matrix[x][y] = DEAD


while True:
    for x in range(number_of_cells):
        for y in range(number_of_cells):
            check_neighbours(x, y)
    time.sleep(2)
    os.system('clear')
    print(np.matrix(game_matrix))
