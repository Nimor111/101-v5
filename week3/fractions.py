from Tasks import simplify_fraction


def smallest_denom(a, b):
    if a % b == 0:
        return a
    elif b % a == 0:
        return b
    return a * b


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return simplify_fraction((self.numerator, self.denominator)) == \
            simplify_fraction((other.numerator, other.denominator))

    def __mul__(self, other):
        frac = simplify_fraction((self.numerator * other.numerator,
                                  self.denominator * other.denominator))
        return Fraction(frac[0], frac[1])

    def __add__(self, other):
        mult = smallest_denom(self.denominator, other.denominator)
        frac = simplify_fraction((mult // self.denominator * self.numerator +
                                 mult // other.denominator * other.numerator,
                                 mult))
        return Fraction(frac[0], frac[1])

    def __sub__(self, other):
        mult = smallest_denom(self.denominator, other.denominator)
        frac = simplify_fraction((mult // self.denominator * self.numerator -
                                 mult // other.denominator * other.numerator,
                                 mult))
        return Fraction(frac[0], frac[1])


def main():
    frac = Fraction(1, 1)
    frac2 = Fraction(2, 2)
    print(frac * frac2)
    print(frac + frac2)
    print(frac - frac2)
    print(frac == frac2)


if __name__ == '__main__':
    main()
