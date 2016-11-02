from sys import argv
import re
from functools import reduce


class Polynomial:
    pass


class Monomial:

    def __init__(self, monomial):
        self.monomial = monomial

    def __str__(self):
        return self.monomial

    def __repr__(self):
        return self.__str__()

    def deriv(self):
        pass


class Parser:

    def __init__(self, string_to_parse):
        self.string_to_parse = string_to_parse

    def parse_string(self):
        return self.string_to_parse.split(' + ')

    def parse_monomials(self):
        for el in self.parse_string():
            monomial = []
            monomial.append(re.findall(r'\d+', el))
            monomial.append(re.findall(r'[x]+', el))
            monomial.append(re.findall(r'[\^]+', el))
            monomial[:] = filter(lambda x: x != [], monomial)
            return monomial

    def convert_to_monomial(self):
        return Monomial(self.parse_monomials)


def main():
    parser = Parser('32x^3 + 3x + 1')
    print(parser.parse_string())
    print(parser.parse_monomials())


if __name__ == '__main__':
    main()

