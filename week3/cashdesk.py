class Bill:

    def __init__(self, amount):
        if amount < 0:
            raise ValueError("Must be positive number!")
        elif type(amount) != int:
            raise TypeError("Must be a number!")

        self.amount = amount

    def __str__(self):
        return "A {0}$ bill".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.__str__())


class BatchBill:

    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def total(self):
        return sum([bill.amount for bill in self.bills])

    # makes object iterable
    def __getitem__(self, item):
        return self.bills[item]


class CashDesk:

    def __init__(self, bills=[]):
        self.bills = []

    def take_money(self, money):
        if type(money) == Bill:
            self.bills. append(money)
        elif type(money) == BatchBill:
            for bill in money.bills:
                self.bills.append(bill)
        else:
            raise TypeError("Must be a bill or a batch of bills!")

    def total(self):
        total = 0

        for bill in self.bills:
            if type(bill) == Bill:
                total += bill.amount
            else:
                for b in bill.bills:
                    total += b.amount

        return total

    def inspect(self):
        res = ""
        res += "We have a total of {0}$ in the desk\n".format(self.total())
        res += '''We have the following count of bills, sorted
        in ascending order:'''
        money_holder = {}
        for bill in self.bills:
            if bill not in money_holder.keys():
                money_holder[bill] = 1
            else:
                money_holder[bill] += 1
        money_holder_keys = sorted(bill.amount for bill in money_holder.keys())
        for el in money_holder_keys:
            res += "\n{0}$ bills - {1}".format(el, money_holder[Bill(el)])

        return res
