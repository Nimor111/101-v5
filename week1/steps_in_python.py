# A function for counting the digits of a number
def sum_of_digits(number):
    sum = 0
    number = abs(number)
    while(number > 0):
        sum += number % 10
        number //= 10
    return sum


print(sum_of_digits(555))


# Create list with the digits of a number
def to_digits(number):
    list = []

    while (number > 0):
        list.append(number % 10)
        number //= 10

    return list


print(to_digits(555))


# Create number from array
def to_number(digits):
    string = ""
    for digit in digits:
        string += str(digit)

    return int(string)


print(to_number([5, 5, 5]))

# Count the vowels in a string


def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = 0
    for letter in string.lower():
        if letter in vowels:
            counter += 1

    return counter


print(count_vowels("AhIOU"))


# Count the consonants in a string
def count_consonants(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = 0
    for letter in string.lower():
        if letter not in vowels:
            counter += 1

    return counter


print(count_consonants("Beginning"))
# Check if a given number is prime


def prime_number(number):
    if (number == 2):
        return True
    for digit in range(2, number):
        if number % digit == 0:
            return False

    return True


print(prime_number(16))
print(prime_number(5))
print(prime_number(4))
print(prime_number(3))
print(prime_number(10))
print(prime_number(7))

# Sum of the factorials of the digits in the number


def fact(n):
    fact = 1
    for num in range(1, n + 1):
        fact *= num

    return fact


def fact_digits(n):
    sum_of_facts = 0

    for digit in to_digits(n):
        sum_of_facts += fact(digit)

    return sum_of_facts


print(fact_digits(555))

# fibonacci sequence


def fibonacci(number):
    prev = 1
    curr = 1

    for num in range(2, number):
        temp = curr
        curr = prev + curr
        prev = temp

    return curr


print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))

# First nth members of Fibonacci


def fibonacci_list(n):
    fib_list = []
    for num in range(1, n + 1):
        fib_list.append(fibonacci(num))
    return fib_list


print(fibonacci_list(1))
print(fibonacci_list(2))
print(fibonacci_list(3))
print(fibonacci_list(10))

# Concatenates first n fibonacci numbers


def fib_number(n):
    result = ""
    for number in range(1, n + 1):
        result += str(fibonacci(number))
    return result


print(fib_number(3))
print(fib_number(10))

# Check if a given string is palindrome


def palindrome(string):
    return string == string[::-1]  # stack overflow rules
    # string[::-1] reverses a string


print(palindrome("1001001"))

# Dictionary with all characters from a string


def char_histogram(string):
    chars_and_occurences = {}
    for char in string:
        if char not in chars_and_occurences.keys():
            chars_and_occurences[char] = 1
        else:
            chars_and_occurences[char] += 1

    return chars_and_occurences


print(char_histogram("Python!"))
print(char_histogram("Alabala"))
