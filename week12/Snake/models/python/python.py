from python.python_body import PythonBody
from python.python_head import PythonHead
from models.vector2D import Vector2D
from models.cell import Cell


class Python(Cell):
    LEFT = Vector2D(0, -1)
    RIGHT = Vector2D(0, 1)
    UP = Vector2D(1, 0)
    DOWN = Vector2D(-1, 0)

    def __init__(self, world, coords, size, direction='U'):
        super().__init__()
        self.world = world
        self.coords = coords
        self.size = size
        self.direction = direction
        self.body = []
        self.head = None
        self.start = Vector2D(self.coords[0], self.coords[1])

    def set_head(self):
        self.head = PythonHead(self.start)
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
                self.start += Python.UP
                cell.vector = self.start
        self.world.add_content(self.body)

    def move(self, direction):
        pass
