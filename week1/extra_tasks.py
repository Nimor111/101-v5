from itertools import combinations_with_replacement
from itertools import groupby
from functools import reduce


def anagrams(word_one, word_two):
    if (len(word_one) != len(word_two)):
        return False

    word_one_dict = {}
    word_two_dict = {}

    for letter in word_one.lower():
        if letter not in word_one_dict.keys():
            word_one_dict[letter] = 1
        else:
            word_two_dict[letter] += 1
    for letter in word_two.lower():
        if letter not in word_two_dict.keys():
            word_two_dict[letter] = 1
        else:
            word_two_dict[letter] += 1
    return word_one_dict == word_two_dict


print(anagrams("Pesho", "Ohsep"))


# gas_stations(320, 90, [50, 80, 140, 180, 220, 290])
def gas_stations(distance, tank_size, stations):
    stations.append(distance)
    if stations[0] > tank_size:
        print("You can't get to the first gas station mate.")

    shortest_list = []
    prev_station = 0
    passed_station = 0
    for station in stations:
        if station - prev_station >= tank_size:
            shortest_list.append(passed_station)
            prev_station = passed_station
        passed_station = station
    return shortest_list


print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))


def is_prime(n):
    if (n == 2):
        return True
    for digit in range(2, n):
        if n % digit == 0:
            return False

    return True


def goldbach(n):
    primes = [i for i in range(2, n) if is_prime(i)]
    # generates combinations that allow repeating elements
    return [i for i in list(combinations_with_replacement(primes, 2))
            if sum(i) == n]


print(goldbach(4))
print(goldbach(6))
print(goldbach(8))
print(goldbach(10))
print(goldbach(100))


def is_credit_card_valid(number):
    list_to_check = [int(i) for i in list(str(number))]

    for idx in range(len(list_to_check[::-1])):
        if idx % 2 == 1:
            list_to_check[idx] *= 2

    return sum([int(i) for i in list(reduce(
                lambda x, y: x + str(y), list_to_check, ''))]) % 10 == 0


print(is_credit_card_valid(79927398713))
print(is_credit_card_valid(79927398715))


def reduce_file_path(path):
    new_path = path.split("/")
    prev = new_path[0]

    for i in range(3):
        for el in new_path:
            if el == "..":
                new_path.remove(prev)
                new_path.remove(el)
            elif el == ".":
                new_path.remove(el)
            prev = el

    new_path = [x if x != '' else "/" for x in new_path]
    for el in range(len(new_path)):
        if new_path[el] != "/":
            new_path.insert(el + 1, "/")
            print(new_path)

#    if new_path[len(new_path) - 1] == "/":
#        new_path.pop()

    return "".join([k for k, g in groupby(new_path)])


print(reduce_file_path("/srv/www/htdocs/wtf/"))
print(reduce_file_path("/srv/../"))
print(reduce_file_path("/srv/www/htdocs/wtf/"))
print(reduce_file_path("/srv/www/htdocs/wtf"))
print(reduce_file_path("/srv/./././././"))
print(reduce_file_path("/etc//wtf/"))
print(reduce_file_path("/etc/../etc/../etc/../"))
print(reduce_file_path("//////////////"))
print(reduce_file_path("/../"))
