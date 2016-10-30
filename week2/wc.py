# word_counter.py
from sys import argv


def word_counter():
    with open(argv[2], 'r') as f:
        lines = f.readlines()

    if argv[1] == 'lines':
        return len(lines)
    elif argv[1] == 'words':
        return len(str(lines).split(' '))
    elif argv[1] == 'chars':
        length = 0
        for el in str(lines).split(' '):
            length += len(el) + 1
        return length - len(lines) * 3

    return "ERR"


print(word_counter())
