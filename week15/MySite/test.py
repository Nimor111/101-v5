import re


def DRLE(string):
    decoded = ''
    chars, nums = [], []
    for c in string:
        if re.search(r'[0-9]', c):
            nums.append(c)
        else:
            chars.append(c)
    for c, n in zip(chars, nums):
        decoded += c * int(n)

    return decoded


print(DRLE('5a2b'))
