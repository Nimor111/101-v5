# sum_numbers.py
from sys import argv


def sum_numbers():
    sum_ = 0
    with open(argv[1], 'r') as f:
        sum_ = sum([int(x) for x in f.read().split(" ") if not x == ''])

    return sum_


def main():
    print(sum_numbers())


if __name__ == '__main__':
    main()
