from settings import symbols
from models.cell import Cell
from python.python_part import PythonPart
from models.food import Food
from models.vector2D import Vector2D


class PythonBody(Cell, PythonPart):

    def __init__(self, v=None):
        super().__init__(vector=v)
        self.contents = self
        self.symbol = symbols.BODY


def main():
    pb = PythonBody(Vector2D(1, 2))
    print(pb.vector)
    print("it works.")


if __name__ == '__main__':
    main()
