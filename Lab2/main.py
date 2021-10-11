#    1. Write a function to return a list of the first n numbers in the Fibonacci string.

# def fib(n):
#     fib_list = [0, 1]
#     a = 0
#     b = 1
#     fib_list = [a, b]
#     index = 2
#     while index != n:
#         c = a + b
#         a = b
#         b = c
#         fib_list.append(c)
#         index += 1
#
#     return fib_list
#
#
# input_nr = input("Enter a number: ")
# number = int(input_nr)
# print(fib(number))


# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

# def is_prime(number):
#     for div in range(2, number):
#         if number % div == 0:
#             return False
#     else:
#         return True
#
#
# def make_prime_list(nr_list):
#     prime_list = []
#     for element in nr_list:
#         if is_prime(element):
#             prime_list.append(element)
#     return prime_list
#
#
# input_var = input("Enter numbers separated by space: ")
# numbers_list = input_var.split()
#
# for index in range(0, len(numbers_list)):
#     numbers_list[index] = int(numbers_list[index])
#
# pr_list = make_prime_list(numbers_list)
# print(pr_list)


#   3. Write a function that receives as parameters two lists a and b and returns:
#   (a intersected with b, a reunited with b, a - b, b - a)

# def function(a, b):
#     inter_a_b = [x for x in a if x in b]
#     a_minus_b = [x for x in a if x not in b]
#     b_minus_a = [x for x in b if x not in a]
#     reunion_a_b = a + b
#
#     return inter_a_b, reunion_a_b, a_minus_b, b_minus_a
#
#
# list_a, list_b = [1, 2, 3, 4, 5], [3, 6, 7, 8]
#
# print(function(list_a, list_b))

# 4. Write a function that receives as a parameters a list of musical notes (strings),
# a list of moves (integers) and a start position (integer).
# The function will return the song composed by going though the musical
# notes beginning with the start position and following the moves given as parameter.
# 	Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
# 	will return ["mi", "fa", "do", "sol", "re"]

# def compose(notes, moves, start_pos ):


# 5. Write a function that receives as parameter a matrix
#  and will return the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).


# N = int(input("Enter the number of rows and columns:"))
#
# # Initialize matrix
# matrix = []
# print("Enter the entries row wise:")
#
# # For user input
# for i in range(N):  # A for loop for row entries
#     a = []
#     for j in range(N):  # A for loop for column entries
#         a.append(int(input()))
#     matrix.append(a)
#
# for i in range(N):
#     for j in range(N):
#         if i > j:
#             matrix[i][j] = 0
# print(matrix)

# 6. Write a function that receives as a parameter a variable number of lists and a whole number x.
# Return a list containing the items that appear exactly x times in the incoming lists.

# Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2 lists
# [1,2,3 ] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2.

# dictionary = {
#
# }
#
#
# def func_x_times(x, *args):
#     new_list_x_times = []
#     for nr_list in args:
#         for el_list in nr_list:
#             key = el_list
#             if key in dictionary:
#                 dictionary[key] += 1
#             else:
#                 dictionary.update({key: 1})
#     for letter, value in dictionary.items():
#         if value == x:
#             new_list_x_times.append(letter)
#     return new_list_x_times
#
#
# new_list = func_x_times(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"])
# print(list(new_list))


# 7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2
# elements. The first element of the tuple will be the number of palindrome numbers found in the list and the second
# element will be the greatest palindrome number.

# def is_palindrome(number):
#     number_copy = number
#     reverse_number = 0
#     while number != 0:
#         reverse_number = (reverse_number * 10) + number % 10
#         number = number // 10
#
#     if number_copy == reverse_number:
#         return True
#     else:
#         return False
#
#
# def palindrome_list(nr_list):
#     p_list = []
#     for elem in nr_list:
#         if is_palindrome(elem):
#             p_list.append(elem)
#
#     count_palindrome = len(p_list)
#     max_palindrome = max(p_list)
#
#     return count_palindrome, max_palindrome
#
#
# print(palindrome_list([123, 121, 456, 1001, 9009]))


# 8  Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set
# to True. For each string, generate a list containing the characters that have the ASCII code divisible by x if the
# flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by x.

# Example: x = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e" .
# Note: The function must return list of lists.


# def func(str_list, x=1, flag=False):
#     list_of_lists = []
#     for word in str_list:
#         wrd_list = []
#         for letter in word:
#             if flag is False and ord(letter) % x == 1:
#                 wrd_list.append(letter)
#             elif flag is True and ord(letter) % x == 0:
#                 wrd_list.append(letter)
#         list_of_lists.append(wrd_list)
#     return list_of_lists
#
#
# print(func(["test", "hello", "lab002"], 2, False))
