from copy import deepcopy
from python.python_body import PythonBody
from python.python_head import PythonHead
from models.vector2D import Vector2D
from models.cell import Cell


class Python(Cell):
    LEFT = Vector2D(0, -1)
    RIGHT = Vector2D(0, 1)
    UP = Vector2D(-1, 0)
    DOWN = Vector2D(1, 0)

    def __init__(self, world, coords, size, direction='U'):
        super().__init__()
        self.world = world
        self.coords = coords
        self.size = size
        self.direction = direction
        self.body = []
        self.start = Vector2D(self.coords[0], self.coords[1])
        self.dead = 0

    def kill(self):
        self.dead = 1

    def is_dead(self):
        return self.dead == 1

    def set_head(self, direction=Vector2D(0, 0)):
        self.start = self.start + direction
        self.head = PythonHead(self.start)
        if (self.head.vector.x < 0 or self.head.vector.x > self.size or
           self.head.vector.y < 0 or self.head.vector.y > self.size):
            return self.kill()
        self.world.set_cell(self.head)

    def change_start(self, new_coords):
        self.start = Vector2D(new_coords[0], new_coords[1])

    def reset_start(self):
        self.start = self.head.vector

    def body_coords(self):
        pass

    def set_body(self):
        self.body = [PythonBody() for _ in range(self.size - 1)]
        if self.direction == 'u' or self.direction == 'U':
            for cell in self.body:
                self.start += Python.DOWN
                cell.vector = self.start
        self.world.add_content(self.body)

    def __choose_direction(self, direction):
        if direction == 'u' or direction == 'U':
            return Python.UP
        elif direction == 'd' or direction == 'D':
            return Python.DOWN
        elif direction == 'l' or direction == 'L':
            return Python.LEFT
        elif direction == 'r' or direction == 'R':
            return Python.RIGHT

    def add_and_delete_last(self, last):
        self.world.add_content(self.body)
        self.world.set_cell(last.empty_cell())

    def move(self, direction):
        self.reset_start()
        self.head.empty_cell()
        last = deepcopy(self.body[-1])
        if direction == 'l' or direction == 'L':
            self.set_head(Python.LEFT)
        elif direction == 'r' or direction == 'R':
            self.set_head(Python.RIGHT)
        elif direction == 'u' or direction == 'U':
            self.set_head(Python.UP)
        elif direction == 'd' or direction == 'D':
            self.set_head(Python.DOWN)
        for cell in self.body:
            cell.vector += self.__choose_direction(direction)
        self.add_and_delete_last(last)
