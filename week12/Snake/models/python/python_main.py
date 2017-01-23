from models.python.python_body import PythonBody
from models.python.python_head import PythonHead

from models.vector2D import Vector2D
from models.cell import Cell
from models.wall import Wall
from models.food import Food
from models.black_hole import BlackHole

from exceptions.exceptions import DirectionError

from context_managers.context_managers import food_log


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
        self.food_flag = False

    def kill(self):
        self.dead = 1

    def is_dead(self):
        return self.dead == 1

    def set_head(self, direction=Vector2D(0, 0)):
        self.start = self.start + direction
        self.head = PythonHead(self.start)
        if self.head.vector.x < 0 or self.head.vector.x >= self.world.size or\
           self.head.vector.y < 0 or self.head.vector.y >= self.world.size:
            return self.kill()
        if isinstance(self.world[self.head.vector.x][self.head.vector.y]
           .contents, Wall) or isinstance(self.world[self.head.vector.x]
           [self.head.vector.y].contents, BlackHole):
            return self.kill()
        try:
            if isinstance(self.world[self.head.vector.x][self.head.vector.y],
                          PythonBody):
                raise DirectionError
        except DirectionError:
            print("WRONG DIRECTION!")
            return self.kill()
        if (isinstance(self.world[self.head.vector.x][self.head.vector.y]
           .contents, Food)):
            with food_log('food_log.txt', 'a') as f:
                pass
            self.food_flag = True
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

    def direction_by_ascii_code(self, direction):
        if ord(direction) == 97:
            return "left"
        elif ord(direction) == 100:
            return "right"
        elif ord(direction) == 119:
            return "up"
        elif ord(direction) == 115:
            return "down"

    def move(self, direction):
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
        if not self.food_flag:
            self.empty_last()
            self.body_coords.pop()
        else:
            self.food_flag = False
        self.world.set_cell(self.head)
        i = 1
        for cell in self.body:
            cell.vector = self.body_coords[i]
            i += 1
        self.world.add_content(self.body)
