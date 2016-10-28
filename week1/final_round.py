import re
from itertools import groupby


def is_number_balanced(n):
    digits = [int(i) for i in str(n)]
    left = digits[:len(digits) // 2:]
    if len(digits) % 2 == 0:
        right = digits[len(digits) // 2:len(digits)]
    else:
        right = digits[len(digits) // 2 + 1:len(digits)]

    return sum(left) == sum(right)


# Mine test, my own, my precious
print(is_number_balanced(121))
print(is_number_balanced(4518))
print(is_number_balanced(1238033))


def increasing_or_decreasing(seq):
    prev = seq[0]
    flag_UP = True
    flag_DOWN = True
    for el in seq[1:]:
        if el > prev:
            prev = el
            flag_DOWN = False
        elif el < prev:
            prev = el
            flag_UP = False
        else:
            flag_DOWN = flag_UP = False

    if flag_DOWN:
        return "Down!"
    elif flag_UP:
        return "UP!"
    else:
        return "False"


print(increasing_or_decreasing([1, 2, 3, 4, 5]))
print(increasing_or_decreasing([5, 6, -10]))
print(increasing_or_decreasing([1, 1, 1, 1]))
print(increasing_or_decreasing([9, 8, 7, 6]))


def get_largest_palindrome(n):
    # return max([i for i in range(n) if str(i) == str(i)[::-1]])
    for el in range(n, -1, -1):
        if str(el) == str(el)[::-1]:
            return el


print(get_largest_palindrome(99))
print(get_largest_palindrome(252))
print(get_largest_palindrome(994687))
print(get_largest_palindrome(754649))


def sum_of_numbers(st):
    return sum([int(i) for i in re.findall('(\d+)', st)])


print(sum_of_numbers("ab125cd3"))
print(sum_of_numbers("ab12"))
print(sum_of_numbers("ab"))


def birthday_ranges(birthdays, ranges):
    res = [0 for i in range(len(ranges))]
    for el in birthdays:
        for i in ranges:
            if el in range(i[0], i[1] + 1):
                res[ranges.index(i)] += 1
    return res


print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3),
                      (1, 4), (1, 5), (4, 6)]))


def numbers_to_message(pressed_sequence):
    result = ""
    is_capital = False
    keyboard = {0: ' ',
                2: ['a', 'b', 'c'],
                3: ['d', 'e', 'f'],
                4: ['g', 'h', 'i'],
                5: ['j', 'k', 'l'],
                6: ['m', 'n', 'o'],
                7: ['p', 'q', 'r', 's'],
                8: ['t', 'u', 'v'],
                9: ['w', 'x', 'y', 'z']}

    # returns list of lists - [digit, number of its occurences]
    grouped_list = [[k, sum(1 for i in g)] for k, g in
                    groupby(pressed_sequence)]
    for el in grouped_list:
        # capitalize letter if 1 in list
        if el[0] == 1:
            is_capital = True
            continue
        # if clicked more than three times start over
        # -4 because list indexes start from 0
        if el[1] > 3:
            el[1] = el[1] - 4
        # space if 0 in list
        if el[1] == 0:
            result += keyboard[0]
        # take values from keyboard dict
        if el[0] != -1:
            if is_capital:
                result += keyboard[el[0]][el[1] - 1].upper()
                is_capital = False
            else:
                result += keyboard[el[0]][el[1] - 1]
    return result


# "abc"
print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))
# "Ivo e Panda"
print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1,
                          7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))


def message_to_numbers(message):
    res_list = []

    keyboard = {0: ' ',
                2: ['a', 'b', 'c'],
                3: ['d', 'e', 'f'],
                4: ['g', 'h', 'i'],
                5: ['j', 'k', 'l'],
                6: ['m', 'n', 'o'],
                7: ['p', 'q', 'r', 's'],
                8: ['t', 'u', 'v'],
                9: ['w', 'x', 'y', 'z']}

    prev_element = None
    for el in list(message):
        if el == " ":
            res_list.append(0)
        else:
            if el.isupper() is True:
                res_list.append(1)
                el = el.lower()
            for element in keyboard.items():
                if el in element[1]:
                    if prev_element == element[0]:
                        res_list.append(-1)
                    for i in range(element[1].index(el) + 1):
                        res_list.append(element[0])
                    prev_element = element[0]
    return res_list


print(message_to_numbers("abc"))
print(message_to_numbers("a"))
print(message_to_numbers("Ivo e Panda"))
print(message_to_numbers("aabbcc"))
