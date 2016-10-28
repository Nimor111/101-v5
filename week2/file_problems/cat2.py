# cat2.py
import sys


def read_files():
    for i in range(1, len(sys.argv)):
        with open(sys.argv[i], "r") as f:
            print(f.read())


def main():
    read_files()


if __name__ == '__main__':
    main()
