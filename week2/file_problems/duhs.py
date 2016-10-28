# duhs.py
import os
from sys import argv


class FileNotFoundError(OSError):
    pass


def convert_bytes(num):
    for x in ['B', 'K', 'M', 'G', 'T']:
        if num < 1024:
            if argv[1] == "-h":
                return str(num) + x
            else:
                return str(num)
        num //= 1024


def find_size():
    size = 0
    file_to_walk = argv[2]
    if argv[1] == "-h":
        file_to_walk = argv[2]
    else:
        file_to_walk = argv[1]
    try:
        for root, dirs, files in os.walk(file_to_walk):
            for name in files:
                try:
                    size += os.path.getsize(os.path.join(root, name))
                except FileNotFoundError:
                    pass
            for name in dirs:
                try:
                    size += os.path.getsize(os.path.join(root, name))
                except FileNotFoundError:
                    pass
    except FileNotFoundError:
            pass
    return convert_bytes(size)


def main():
    print(find_size())


if __name__ == '__main__':
    main()
