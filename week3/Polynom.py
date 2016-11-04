from sys import argv
import re
from functools import reduce


# for future stuff
SYMBOLS = [" + ", " - "]


class Polynomial:

    def __init__(self, parser):
        self.parser = parser

    def construct_polynom(self):
        monomials = self.parser.parse_monomials()
        # return monomials
        return [Monomial(el).deriv() for el in monomials]

    def to_string(self):
        poly = self.construct_polynom()
        for iterator in range(len(poly)):
            if type(poly[iterator]) == list:
                poly[iterator].insert(1, "*")
                for i in range(len(poly[iterator])):
                    if poly[iterator][i] == ['x'] \
                       or poly[iterator][i] == ['^']:
                        poly[iterator][i] = "".join(poly[iterator][i])
        return poly

    def __str__(self):
        poly = self.to_string()
        polynomial = ""
        for iterator in range(len(poly)):
            polynomial += "".join(poly[iterator]) + " + "
        if len(polynomial) > 4:  # because it's ' 0 + '
            return polynomial.strip(" + 0")
        else:
            return polynomial.strip(" + ")

    def __repr__(self):
        return self.__str__()


class Monomial:

    def __init__(self, monomial):
        self.monomial = monomial

    def __str__(self):
        return "Monomial: {}".format(self.monomial)

    def __repr__(self):
        return self.__str__()

    def deriv(self):
        if len(self.monomial) == 1 and self.monomial[0] == ['x']:
            self.monomial = str(1)
        elif len(self.monomial) == 1:
            self.monomial = str(0)
        elif len(self.monomial) == 2:
            self.monomial = "".join(self.monomial[0])
        else:
            self.monomial.append(str(int(self.monomial[0][1]) - 1))
            self.monomial[0] = str(reduce(lambda x, y: int(x) * int(y),
                                          self.monomial[0]))
        return self.monomial


class Parser:

    def __init__(self, string_to_parse):
        self.string_to_parse = string_to_parse

    def parse_string(self):
        return self.string_to_parse.split(' + ')

    def parse_monomials(self):
        monomials = []
        for el in self.parse_string():
            monomials.append(self.convert_to_monomial(el))
        return monomials

    def convert_to_monomial(self, string):
        monomial = []
        monomial.append(re.findall(r'\d+', string))
        monomial.append(re.findall(r'[x]+', string))
        monomial.append(re.findall(r'[\^]+', string))
        monomial[:] = filter(lambda x: x != [], monomial)
        # insert 1 for easier calculating
        if len(monomial[0]) == 1 and ['x'] in monomial[0]:
            monomial[0].insert(0, str(1))
        return monomial

    def return_monomial(self, idx):
        try:
            return self.parse_monomials()[idx - 1]
        except IndexError as e:
            print(e)


def main():
    parser = Parser(argv[1])
    # print(parser.parse_string())
    # print(parser.parse_monomials())
    # m = Monomial(parser.convert_to_monomial())
    # print(m)
    # m = Monomial(parser.return_monomial(1))
    # print(m)
    # print(m.deriv())
    # print([reduce(lambda x, y: x * y, [32, 3])])
    poly = Polynomial(parser)
    # print(poly.construct_polynom())
    # print(poly.to_string())
    print(poly)


if __name__ == '__main__':
    main()
