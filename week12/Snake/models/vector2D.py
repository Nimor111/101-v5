class Vector2D:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, num):
        return Vector2D(self.x * num, self.y * num)

    def __truediv__(self, num):
        return Vector2D(self.x / num, self.y / num)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return self.__str__()


def main():
    pass


if __name__ == '__main__':
    main()
