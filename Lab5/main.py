import utils as ut
import app as a


def ex2(*args, **kwargs):
    """Create a function and an anonymous function that receive a variable number of arguments. Both will return the
    sum of the values of the keyword arguments. """
    sum_args = 0
    for arg in args:
        sum_args += arg

    for var, value in kwargs.items():  # for default variables
        sum_args += value
    return sum_args


def ex3(input_str):
    """3) Using functions, anonymous functions, list comprehensions and filter, implement three methods to generate a
    list with all the vowels in a given string.

For the string "Programming in Python is fun" the list returned will be ['o', 'a', 'i', 'i', 'o', 'i', 'u']."""

    vowel_str = "aeiouAEIOU"
    vowels_list = list()
    for letter in input_str:
        if letter in vowel_str:
            vowels_list.append(letter)
    return vowels_list


def ex4(*args, **kwargs):
    """Write a function that receives a variable number of arguments and keyword arguments. The function returns a
    list containing only the arguments which are dictionaries, containing minimum 2 keys and at least one string key
    with minimum 3 characters. """

    list_of_args = list()
    for arg in args:
        flag = 0
        if isinstance(arg, dict):
            for key, value in arg.items():
                if isinstance(key, str) and len(key) >= 3:
                    flag = 1
            if len(arg.keys()) < 2:
                flag = 0
        if flag == 1:
            list_of_args.append(arg)

    for dic in kwargs.values():
        flag = 0
        if isinstance(dic, dict):
            for key, value in dic.items():
                if isinstance(key, str) and len(key) >= 3:
                    flag = 1
            if len(dic.keys()) < 2:
                flag = 0
            if flag == 1:
                list_of_args.append(dic)
    return list_of_args


def ex5(args_list):
    """ Write a function with one parameter which represents a list.
    The function will return a new list containing all the numbers found in the given list.
Example: my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]) will return [1, 5, 6, 3.0]"""
    nr_list = list()
    for elem in args_list:
        if isinstance(elem, int) or isinstance(elem, float) or isinstance(elem, complex):
            nr_list.append(elem)
    return nr_list


def ex6(nr_list):
    """Write a function that receives a list with integers as parameter
     that contains an equal number of even and odd numbers that are in no specific order.
     The function should return a list of pairs (tuples of 2 elements) of numbers (Xi, Yi)
      such that Xi is the i-th even number in the list and Yi is the i-th odd number
Example:
my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]) will return [(2, 1), (8, 3), (4, 5), (10, 7), (2, 9)]"""

    odd_list = list(filter(lambda nr: nr % 2 == 1, nr_list))
    even_list = list(filter(lambda nr: nr % 2 == 0, nr_list))

    list_of_tuples = list(zip(even_list, odd_list))

    return list_of_tuples


def sum_digits(x):
    return sum(map(int, str(x)))


def fib_generator():
    a = 0
    b = 1
    fib_list = [a, b]
    index = 2
    while index != 1000:
        c = a + b
        a = b
        b = c
        fib_list.append(c)
        index += 1

    return fib_list


def ex7(**kwargs):
    """The function generates the first 1000 numbers of the Fibonacci sequence and then processes them in the
    following way:

If the function receives a parameter called filters, this will be a list of predicates (function receiving an
argument and returning True/False) and will retain from the generated numbers only those for which the predicates are
True.

If the function receives a parameter called limit, it will return only that amount of numbers from the sequence.

If the function receives a parameter called offset, it will skip that number of entries from the beginning of the result list.

The function will return the processed numbers."""

    fib_list = fib_generator()

    # filters: kwargs[0]
    # limit : kwargs[1]
    # offset: 2

    for key, value in kwargs.items():
        if key == "filters":
            for val in value:
                fib_list = list(filter(val, fib_list))
        elif key == "offset":
            fib_list = fib_list[value:]
        elif key == "limit":
            fib_list = fib_list[:value]

    return fib_list


def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b


def print_arguments(func):
    # storing the function in a variable
    # if func == "multiply_by_two":
    #     print("The arguments are: ", x, " and will return ", func(x))
        return func(x)


if __name__ == '__main__':
    # ex1
    # nr = input("Enter a number: ")
    # print(ut.process_item(int(nr)))
    # a.process_item()

    # ex2
    # print(ex2(1, 2, c=3, d=4))
    # ex2_anon = lambda *args, **def_args: sum(args) + sum(def_args.values())
    # print(ex2_anon(1, 2, 3, c=3))

    # ex3
    # in_str = input("Enter a string: ")
    # print(ex3(in_str))  # with function

    # list_vow = list() # with anonymous function
    # ex3_anon = lambda input_str: {list_vow.append(letter) for letter in input_str if letter in "aeiouAEIOU"}
    # ex3_anon(in_str)
    # print(list_vow)

    # new_list = filter(lambda letter: letter in "aeiouAEIOU", in_str)  # with list comprehension and filter
    # print(list(new_list))

    # ex4

    # print(ex4({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764,
    #           dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True}))

    # ex5

    # print(ex5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))

    # ex6

    # print(ex6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))

    # ex7
    # print(ex7(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
    #           offset=2,
    #           limit=2))

    # ex8a

    augmented_multiply_by_two = print_arguments(multiply_by_two)

    x = augmented_multiply_by_two(10)  # this will print: Arguments are: (10,), {} and will return 20.

    # augmented_add_numbers = print_arguments(add_numbers)
    #
    # x = augmented_add_numbers(3, 4)  # this will print: Arguments are: (3, 4), {} and will return 7.
