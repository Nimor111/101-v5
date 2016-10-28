# first_name = input("Please, input your name: ")
# print(first_name)

# For loop

# for letter in first_name:
# 	print(letter*3)

list_of_numbers = [5, 3, 8, 9, 2, 6, 1, 44]

# for element in list_of_numbers:
# 	element = element**2

# for iter in list_of_numbers:
# 	iter *= 2

# print(list_of_numbers)

# for iter in range(len(list_of_numbers)):
# 	list_of_numbers[iter] *= 2

# print(list_of_numbers)

# While loop

# If statement

# for element in list_of_numbers:
# 	if element % 2 == 0:
# 		print(element)

# create function

def function_1(list_of_numbers):
	for element in list_of_numbers:
	    if element % 2 == 0:
		    print(element)

	return list_of_numbers

print(function_1(list_of_numbers))