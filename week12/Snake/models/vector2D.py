class Vector2D:

    def __init__(self, x, y):
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


def main():
    pass


if __name__ == '__main__':
    main()
