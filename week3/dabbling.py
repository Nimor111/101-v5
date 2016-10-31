a = [1, 2, 3, 4]
a[:] = map(lambda x: x ** 2, a)
print(a)

a[:] = filter(lambda x: x % 2 == 0, a)
print(a)
