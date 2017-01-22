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
        self.body_coords = [Vector2D() for _ in range(self.size)]

    def kill(self):
        self.dead = 1

    def is_dead(self):
        return self.dead == 1

    def set_head(self, direction=Vector2D(0, 0)):
        self.start = self.start + direction
        self.head = PythonHead(self.start)
        if (self.head.vector.x < 0 or self.head.vector.x > self.world.size or
           self.head.vector.y < 0 or self.head.vector.y > self.world.size):
            print("Killing python...", self.head.vector.x,
                  self.head.vector.y)
            return self.kill()
        self.body_coords[0] = self.head.vector
        self.world.set_cell(self.head)

    def change_start(self, new_coords):
        self.start = Vector2D(new_coords[0], new_coords[1])

    def reset_start(self):
        self.start = self.head.vector

    def empty_last(self):
        c = Cell(vector=self.body_coords[-1])
        self.world.set_cell(c)

    def get_body_coords(self):
        return [str(i) for i in self.body_coords]

    def set_body(self):
        self.body = [PythonBody() for _ in range(self.size - 1)]
        i = 1
        if self.direction == 'u' or self.direction == 'U':
            for cell in self.body:
                self.start += Python.DOWN
                cell.vector = self.start
                self.body_coords[i] = cell.vector
                i += 1
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

    def move(self, direction):
        self.reset_start()
        self.body_coords.insert(1, self.head.vector)
        if direction == 'l' or direction == 'L':
            self.set_head(Python.LEFT)
        elif direction == 'r' or direction == 'R':
            self.set_head(Python.RIGHT)
        elif direction == 'u' or direction == 'U':
            self.set_head(Python.UP)
        elif direction == 'd' or direction == 'D':
            self.set_head(Python.DOWN)
        self.empty_last()
        self.body_coords.pop()
        self.world.set_cell(self.head)
        i = 1
        for cell in self.body:
            cell.vector = self.body_coords[i]
            i += 1
        self.world.add_content(self.body)
        print("Head coords: ", str(self.head.vector))
