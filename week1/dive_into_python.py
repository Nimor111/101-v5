from itertools import groupby


def count_substrings(haystack, needle):
    return haystack.count(needle)


# not a good solution
def count_substrings2(haystack, needle):
    return len([i for i in haystack.split(needle) if i.strip == ''])


print(count_substrings("This is a test string", "is"))
print(count_substrings("babababa", "baba"))
print(count_substrings("Python is an awesome language to program in!", "o"))
print(count_substrings("We have nothing in common!", "really?"))


def sum_matrix(m):
    sum = 0
    for row in m:
        for col in row:
            sum += col
    return sum


def sum_matrix_2(m):
    return sum([sum(sub_list) for sub_list in m])


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sum_matrix(m))
print(sum_matrix_2(m))


def nan_expand(n):
    if n == 0:
        return ""
    if n == 1:
        return " Not a NaN"
    return " Not a" + nan_expand(n - 1)


def nan_expand_2(n):
    return "Not a " * n + "NaN"


print(nan_expand_2(3))


def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    for num in range(2, n - 1):
        if n % num == 0:
            return False
    return True


# print(is_prime(5))
# print(is_prime(6))
# print(is_prime(11))


def prime_factorization(n):
    primes = [x for x in range(n) if is_prime(x) is True]
    fact_dict = {}
    flag = True
    multip = 1

    while(flag is True):
        for el in primes:
            if (n % el == 0):
                multip *= el
                if el not in fact_dict.keys():
                    fact_dict[el] = 1
                else:
                    fact_dict[el] += 1
            if multip == n:
                flag = False
                break

    return [(k, v) for k, v in fact_dict.items()]


print(prime_factorization(356))


# group([1, 1, 1, 2, 3, 1, 1]) == [[1, 1, 1], [2], [3], [1, 1]]

def group(listy):
    listy.append([])
    res_list = []
    current = listy[0]
    count = 0
    for value in listy:
        if value == current:
            count += 1
        else:
            temp_list = []
            for num in range(count):
                temp_list.append(current)
            current = value
            count = 1
            res_list.append(temp_list)
    return res_list


print(group([1, 2, 1, 2, 3, 3]))


def max_consecutive(items):
    grouped_list = [(k, sum(1 for i in g)) for k, g in groupby(items)]
    max_cons_values = []
    for lists in grouped_list:
        max_cons_values.append(lists[1])

    return max(max_cons_values)


print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))


def word_counter():
    counter = 0
    word = input("Enter word: ")
    rows, cols = input().split()
    rows = int(rows)
    cols = int(cols)
    if len(word) > rows or len(word) > cols:
        print("Invalid number of rows or columns!")
        return 0
    m = [input().strip().split() for i in range(rows)]
    for row in m:
        if word in ''.join(row):
            counter += 1
        if word in ''.join(row)[::-1]:
            counter += 1
    for cols in range(cols):
        if word in ''.join([row[cols] for row in m]):
            counter += 1
        if word in ''.join([row[cols] for row in m])[::-1]:
            counter += 1
    for row in range(1):
        for col in range(cols):
            if word in ''.join([m[row + count][col + count] for count in
                                range(max(rows, cols))
                                if row + count < rows and col + count < cols]):
                counter += 1
            if word in ''.join([m[row + count][col + count] for count in
                                range(max(rows, cols))
                                if row + count < rows and
                                col + count < cols])[::-1]:
                counter += 1
    for row in range(rows - 1, rows):
        for col in range(cols + 1):
            if word in ''.join([m[row - count][col + count] for count in
                                range(max(rows, cols))
                                if row - count >= 0 and col + count < cols]):
                counter += 1
    for row in range(rows - 1, rows):
        for col in range(cols, -1, -1):
            if word in ''.join([m[row - count][col - count] for count in
                                range(max(rows, cols))
                                if row - count >= 0 and col - count >= 0]):
                counter += 1
        if word == word[::-1]:
            counter //= 2
        return counter


print(word_counter())
