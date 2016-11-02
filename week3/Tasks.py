def gcd(a, b):
    if a == b:
        return a
    else:
        if a > b:
            return gcd(a - b, b)
        else:
            return gcd(a, b - a)


def gcd_second(a, b):
    if b == 0:
        return a
    else:
        return gcd_second(b, a % b)


def simplify_fraction(fraction):
    if fraction[0] == fraction[1]:
        return 1
    if fraction[0] == 0:
        return 0
    if fraction[1] == 0:
        raise ZeroDivisionError
    return (fraction[0] // gcd_second(fraction[0], fraction[1]),
            fraction[1] // gcd_second(fraction[0], fraction[1]))


def sort_fractions(fractions):
    return [j[1] for j in sorted([(i[0] / i[1], i) for i in fractions])]


def main():
    print(simplify_fraction((3, 9)))
    print(simplify_fraction((1, 7)))
    print(simplify_fraction((4, 10)))
    print(simplify_fraction((63, 462)))
    print(sort_fractions([(2, 3), (1, 2)]))
    print(sort_fractions([(2, 3), (1, 2), (1, 3)]))
    print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8),
                          (9, 6), (15, 32)]))


if __name__ == '__main__':
    main()
