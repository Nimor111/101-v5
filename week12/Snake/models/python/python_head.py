from settings import symbols
from models.cell import Cell
from python.python_part import PythonPart
from models.food import Food


class PythonHead(Cell, PythonPart):

    def __init__(self, vector):
        super().__init__(vector=vector)
        self.contents = self
        self.symbol = symbols.HEAD


def main():
    pass


if __name__ == '__main__':
    main()
