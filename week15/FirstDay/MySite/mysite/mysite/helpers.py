import re
from itertools import groupby


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def nth_fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b

    return a


def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def n_prime_numbers(n):
    primes = []
    i = 1
    num = 2
    while i <= n:
        if is_prime(num):
            primes.append(num)
            i += 1
        num += 1
    return primes


def RLE(string):
    return [(x, len(list(xs))) for x, xs in groupby(string)]


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
