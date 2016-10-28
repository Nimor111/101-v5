# generate_numbers.py
import sys
from random import randint


def generate_ints():
    with open(sys.argv[1], "w") as f:
        for i in range(1, int(sys.argv[2]) + 1):
            f.write(" " + str(randint(1, 1000)))


def main():
    generate_ints()


if __name__ == '__main__':
    main()
