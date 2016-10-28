# cat.py
import sys


def read_file():
    with open(sys.argv[1], "r") as f:
        print(f.read())


def main():
    read_file()


if __name__ == '__main__':
    main()
