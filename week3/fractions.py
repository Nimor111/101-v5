from Tasks import simplify_fraction


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
        if type(frac) != tuple:
            return frac
        if frac[1] == 1:
            return frac[0]
        return Fraction(frac[0], frac[1])

    def smallest_denom(self, a, b):
        if a % b == 0:
            return a
        elif b % a == 0:
            return b
        return a * b

    def __add__(self, other):
        add = self.smallest_denom(self.denominator, other.denominator)
        frac = simplify_fraction((add // self.denominator * self.numerator +
                                 add // other.denominator * other.numerator,
                                 add))
        if type(frac) != tuple:
            return frac
        if frac[1] == 1:
            return frac[0]
        return Fraction(frac[0], frac[1])

    def __sub__(self, other):
        sub = self.smallest_denom(self.denominator, other.denominator)
        frac = simplify_fraction((sub // self.denominator * self.numerator -
                                 sub // other.denominator * other.numerator,
                                 sub))
        if type(frac) != tuple:
            return frac
        if frac[1] == 1:
            return frac[0]
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
