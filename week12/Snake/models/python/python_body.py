from settings import symbols
from models.cell import Cell
from python.python_part import PythonPart
from models.food import Food


class PythonBody(Cell, PythonPart):

    def __init__(self, vector=None):
        super().__init__(vector=vector)
        self.contents = self
        self.symbol = symbols.BODY


def main():
    pb = PythonBody(3)
    print("it works.")


if __name__ == '__main__':
    main()
