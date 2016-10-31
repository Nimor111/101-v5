from cashdesk import Bill, BatchBill, CashDesk

# Bill tests
bill = Bill(12)
some_bill = Bill(6)
bill2 = Bill(12)
print(int(bill))
print(str(bill))
print(bill)
print(bill == bill2)
print(bill == some_bill)

money_holder = {}
money_holder[bill] = 1

if bill2 in money_holder:
    money_holder[bill2] += 1

print(money_holder)
# Bill tests

# BatchBill tests
values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)
print(batch.total())
for bill in batch:
    print(bill)
# BatchBill tests

# CashDesk tests
desk = CashDesk()
values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)

desk.take_money(batch)
desk.take_money(Bill(10))

print(desk.total())
print(desk.inspect())
# CashDesk tests
