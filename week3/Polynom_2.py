class Polynom:

    def __init__(self, polynom):
        self.polynom = polynom.split('+')

    def combine(self, polynom):
        new_polynom = {}
        for el in polynom:
            if int(el[1]) in new_polynom.keys():
                new_polynom[int(el[1])] += int(el[0])
            else:
                new_polynom[int(el[1])] = int(el[0])
        return new_polynom

    def split_x(self):
        new_polynom = []
        groups = []
        for el in self.polynom:
            groups = el.split('x^')
            if len(groups) == 2:
                if(groups[0] == ''):
                    groups[0] = '1'
            elif(groups[0][-1] == 'x'):
                if groups == ['x']:
                    groups = ['1', '1']
                else:
                    groups[0] = groups[0][0:-1]
                    groups.append('1')
            else:
                continue
            new_polynom.append(groups)
        return sorted(self.combine(new_polynom).items())

    def solve(self):
        res = []
        for power, coeff in self.split_x():
            res.append([int(coeff) * int(power), int(power) - 1])
        return sorted(res)[::-1]

    def beautiful(self):
        pass


def main():
    polynom = Polynom("5x^4+10x^3")
    # print(polynom.combine())
    print(polynom.split_x())
    print(polynom.solve())


if __name__ == "__main__":
    main()
