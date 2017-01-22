from settings import symbols
from models.cell import Cell
from python.python_part import PythonPart
from models.food import Food


class PythonHead(Cell, PythonPart):

    def __init__(self, v):
        super().__init__(vector=v)
        self.contents = self
        self.symbol = symbols.HEAD


def main():
    pass


if __name__ == '__main__':
    main()
