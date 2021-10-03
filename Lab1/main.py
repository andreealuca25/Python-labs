# Ex 1
# Find The greatest common divisor of multiple numbers read from the console.

def gcdfunc(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


# input_var = input("Enter numbers separated by space: ")
# numbers_list = input_var.split()
#
# for index in range(0, len(numbers_list)):
#     numbers_list[index] = int(numbers_list[index])
#
#
# for index in range(0, len(numbers_list) - 2):
#     numbers_list[index + 1] = gcdfunc(numbers_list[index], numbers_list[index + 1])
#
#
# gcd = numbers_list[len(numbers_list)-2]
# print(gcd)


# Ex 2
#  Write a script that calculates how many vowels are in a string.

# input_str = input( "Enter a string: ")
#
# vowelNumber = input_str.count('a') + input_str.count('e') + input_str.count('i') + input_str.count('o') +
# input_str.count('u') + input_str.count('A') + input_str.count('E') + + input_str.count('I') + input_str.count('O')
# +  input_str.count('U')
#
# print(vowelNumber)

# Ex 3
# Write a script that receives two strings and prints the number of occurrences of the first string in the second.

# input_str1 = input( "Enter the first string: ")
# input_str2 = input( "Enter the second string: ")
#
# print(input_str2.count(input_str1))

# Ex 4
# Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

# input_str = input("Enter a string: ")
#
# lowercase_str = ''
# lowercase_str = lowercase_str + input_str[0].lower()
#
# for index in range(1, len(input_str) ):
#     if input_str[index]>='A' and input_str[index]<= 'Z':
#         lowercase_str = lowercase_str + "_" + input_str[index].lower()
#     elif input_str[index]>='a' and input_str[index]<= 'z':
#         lowercase_str = lowercase_str + input_str[index]
#
#
# print(lowercase_str)

# Ex 5 Given a square matrix of characters write a script that prints the string obtained by going through the matrix
# in spiral order (as in the example):

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


# 6
# Write a function that validates if a number is a palindrome.


# def palindrome(number):
#     number_copy = number
#     reverse_number = 0
#     while number != 0:
#         reverse_number = (reverse_number * 10) + number % 10
#         print(reverse_number)
#         number = number // 10
#
#     if number_copy == reverse_number:
#         return True
#     else:
#         return False
#
#
# input_nr = input("Enter a number: ")
# nr = int(input_nr)
#
# print(palindrome(nr))


# Ex 7
# Write a function that extract a number from a text (for example if the text is "An apple is 123 USD",
# this function will return 123, or if the text is "abc123abc" the function will extract 123).
# The function will extract only the first number that is found.

# def extractnumber(str):
#     number_str = ''
#     for index in range(1, len(str)):
#         print(str[index])
#
#         if '0' <= str[index - 1] <= '9':
#             number_str = number_str + str[index - 1]
#             if not ('0' <= str[index] <= '9'):
#                 return number_str
#
#         if index == len(str) - 1:  # checks if the last char is a number
#             if '0' <= str[index - 1] <= '9':
#                 number_str = number_str + str[index]
#
#     return number_str
#
#
# input_str = input("Enter a string: ")
# print(extractnumber(input_str))


# Ex 8 Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary
# format is 00011000, meaning 2 bits with value "1"


# def count_binary_1(bin_num):
#     counter = 0
#     for index in range(len(bin_num)):
#         if bin_num[index] == "1":
#             counter += 1
#     return counter
#
#
# input_nr = input("Enter a number: ")
# number = int(input_nr)
# bin_num = bin(number)
# print(count_binary_1(bin_num))


# Ex 9
# Write a functions that determine the most common letter in a string.
# For example if the string is "an apple is not a tomato", then the most common character is "a" (4 times).
# Only letters (A-Z or a-z) are to be considered.
# Casing should not be considered "A" and "a" represent the same character.

# alphabet = {
#
# }
#
#
# def the_most_common_letter(input_string):
#     for index in range(len(input_string)):
#         key = input_string[index]
#         if 'a' <= key <= 'z' or 'A' <= key <= 'Z':
#             if key in alphabet:
#                 alphabet[key] += 1
#             else:
#                 alphabet.update({key: 1})
#
#     max_letter = ''
#     max_value = -1
#     for letter, value in alphabet.items():
#         if max_value < value:
#             max_value = value
#             max_letter = letter
#
#     return max_letter
#
#
# input_str = input("Enter a string: ")
# print(the_most_common_letter(input_str))

# Ex 10
# Write a function that counts how many words exists in a text.
# A text is considered to be form out of words that are separated by only ONE space.
# For example: "I have Python exam" has 4 words.

# def count_words(input_string):
#     counter = 0
#     for index in range(len(input_string) - 1):
#         if ('a' <= input_string[index] <= 'z' or 'A' <= input_string[index] <= 'Z') and input_string[index + 1] == ' ':
#             counter += 1
#     return counter + 1
#
#
# input_str = input("Enter a string: ")
# print(count_words(input_str))
