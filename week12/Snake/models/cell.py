from models.wall import Wall
from models.food import Food
from settings import symbols


class Cell:

    def __init__(self, contents=None, vector=None):
        self.contents = contents
        if self.contents is None:
            self.symbol = symbols.EMPTY
        elif isinstance(self.contents, Food):
            self.symbol = symbols.FOODS
        elif isinstance(self.contents, Wall):
            self.symbol = symbols.WALL
        if vector is not None:
            self.vector = vector

    def is_empty(self):
        return self.contents is None

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return self.__str__()

    # def set_symbol(self):
    #     if self.contents is None:
    #         self.symbol = □
    #     elif isinstance(self.contents, Food):
    #         self.symbol = 🍌
    #     elif isinstance(self.contents, Wall):
    #         self.symbol = ■
