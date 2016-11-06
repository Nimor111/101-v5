class BankAccount:

    def __init__(self, name, balance, currency, history=[]):
        if balance < 0:
            raise ValueError("Balance must be positive!")
        self.name = name
        self.balance = balance
        self.currency = currency
        self.history = ['Account was created']

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive!")
            return False
        self.balance += amount
        self.history.append('Deposited {}{}'.format(amount, self.currency))
        return True

    def balance_check(self):
        self.history.append('Balance check -> {}{}'
                            .format(self.balance, self.currency))
        return self.balance

    def withdraw(self, amount):
        if amount < 0 or self.balance <= 0 or amount > self.balance:
            self.history.append('Withdraw for {}{} failed.'.format
                                (amount, self.currency))
            return False
        self.balance -= amount
        self.history.append('{}{} was withdrawn'.format(amount, self.currency))
        return True

    def __str__(self):
        return str("Bank account for {} with balance of {}{}".format
                   (self.name, self.balance, self.currency))

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        self.history.append('__int__ check -> {}{}'
                            .format(self.balance, self.currency))
        return int(self.balance)

    def transfer_to(self, account, amount):
        if amount <= 0:
            raise ValueError("Be generous!")
        if self.currency == account.currency and self.balance >= 0:
            account.balance += amount
            self.balance -= amount
            self.history.append('Transfer to {} for {}{}'.format
                                (account.name, amount, self.currency))
            account.history.append('Transfer from {} for {}{}'.format
                                   (self.name, amount, self.currency))
            return True
        else:
            return False

    def history_check(self):
        return self.history


def main():
    # account = BankAccount("Rado", 0, "$", [])
    # print(account)
    # account.deposit(1000)
    # print(account.balance_check())
    # str(account)
    # print(int(account))
    # print(account.history_check())
    # print(account.withdraw(500))
    # print(account.balance_check())
    # print(account.history_check())
    # print(account.withdraw(1000))
    # print(account.balance_check())
    # print(account.history_check())

    rado = BankAccount("Rado", 1000, "BGN")
    ivo = BankAccount("Ivo", 0, "BGN")
    print(rado.transfer_to(ivo, 500))
    print(rado.balance_check())
    print(ivo.balance_check())
    print(rado.history_check())
    print(ivo.history_check())


if __name__ == '__main__':
        main()
