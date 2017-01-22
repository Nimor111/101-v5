from copy import deepcopy
from models.python.python_body import PythonBody
from models.python.python_head import PythonHead
from models.vector2D import Vector2D
from models.cell import Cell
from models.wall import Wall
from models.black_hole import BlackHole


class Python(Cell):
    LEFT = Vector2D(0, -1)
    RIGHT = Vector2D(0, 1)
    UP = Vector2D(-1, 0)
    DOWN = Vector2D(1, 0)

    def __init__(self, world, coords, size, direction):
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
        if (self.head.vector.x < 0 or self.head.vector.x >= self.world.size or
           self.head.vector.y < 0 or self.head.vector.y >= self.world.size):
            return self.kill()
        if (isinstance(self.world[self.head.vector.x][self.head.vector.y]
           .contents, Wall) or isinstance(self.world[self.head.vector.x]
           [self.head.vector.y].contents, BlackHole) or isinstance(
           self.world[self.head.vector.x][self.head.vector.y], PythonBody)):
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

    def get_direction_for_body(self, direction):
        if direction == Python.UP:
            return Python.DOWN
        elif direction == Python.DOWN:
            return Python.UP
        elif direction == Python.LEFT:
            return Python.RIGHT
        elif direction == Python.RIGHT:
            return Python.LEFT

    def set_body(self):
        self.body = [PythonBody() for _ in range(self.size - 1)]
        i = 1
        direction = self.get_direction_for_body(self.direction)
        for cell in self.body:
            self.start += direction
            cell.vector = self.start
            self.body_coords[i] = cell.vector
            i += 1
        self.world.add_content(self.body)

    def find_opposite_direction(self):
        if self.direction == Python.UP:
            return Python.DOWN
        elif self.direction == Python.DOWN:
            return Python.UP
        elif self.direction == Python.LEFT:
            return Python.RIGHT
        elif self.direction == Python.RIGHT:
            return Python.LEFT

    def move(self, direction):
        if direction == self.find_opposite_direction():
            return self.kill()
        self.reset_start()
        self.body_coords.insert(1, self.head.vector)
        if ord(direction) == 97:
            self.set_head(Python.LEFT)
        elif ord(direction) == 100:
            self.set_head(Python.RIGHT)
        elif ord(direction) == 119:
            self.set_head(Python.UP)
        elif ord(direction) == 115:
            self.set_head(Python.DOWN)
        else:
            print("Invalid key! w - up, s - down, a - left, d - right!")
            return
        self.direction = direction
        self.empty_last()
        self.body_coords.pop()
        self.world.set_cell(self.head)
        i = 1
        for cell in self.body:
            cell.vector = self.body_coords[i]
            i += 1
        self.world.add_content(self.body)
