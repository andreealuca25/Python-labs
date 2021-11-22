import os
import re


def ex1(phrase):
    """"Write a function that extracts the words from a given text as a parameter.
    A word is defined as a sequence of alpha-numeric characters."""
    return re.split("\\s", phrase)


def ex2(reg_string, txt_string, x):
    """"Write a function that receives as a parameter a regex string, a text string and a whole number x, and returns
    those long-length x substrings that match the regular expression. """
    expression = reg_string + "{" + str(x) + "}"  # matches x times
    return re.findall(expression, txt_string)


def ex3(txt_str, list_reg_expr):
    """"Write a function that receives as a parameter a string of text characters and a list of regular expressions
    and returns a list of strings that match on at least one regular expression given as a parameter. """
    list_of_matches = list()
    for reg in list_reg_expr:
        result = re.search(reg, txt_str)
        if result != "":
            list_of_matches.append(result.group(0))

    return list_of_matches


def ex4():
    """"Write a function that receives as a parameter the path to an xml document and an attrs dictionary and returns
    those elements that have as attributes all the keys in the dictionary and values the corresponding values. For
    example, if attrs={"class": "url", "name": "url-form", "data-id": "item"} the items selected will be those tags
    whose attributes are class="url" si name="url-form" si data-id="item". """
    pass


def ex5():
    """"are legatura cu ex 4"""
    pass


def ex6(txt_str):
    """"Write a function that, for a text given as a parameter, censures words that begin and end with vowels.
    Censorship means replacing characters from odd positions with *. """
    words = re.findall("\\w+", txt_str)
    for word in words:
        if re.match("^([aeiouAEIOU]).+([aeiouAEIOU])$", word) is not None:
            for index in range(len(word)):
                if index % 2 == 1:
                    word = word[:index] + '*' + word[index + 1:]
            print(word)


def ex7(input_str):
    """"Verify using a regular expression whether a string is a valid CNP."""
    pattern = "^[1-9]\\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\\d|3[01])(0[1-9]|[1-4]\\d|5[0-2]|99)(00[1-9]|0[1-9]\\d|[1-9]\\d\\d)\\d$"
    result = re.match(pattern, input_str)

    if result:
        return True
    else:
        return False


def ex8(directory, regex):
    """"Write a function that recursively scrolls a directory and
    displays those files whose name matches a regular expression given as a parameter or contains a string
     that matches the same expression. Files that satisfy both conditions will be prefixed with ">>"""""
    for _, directories, filenames in os.walk(directory):
        for directory in directories:
            print(directory)
        for filename in filenames:
            if re.match(regex, filename):
                print(">>" + filename)
            else:
                print(filename)


if __name__ == '__main__':
    # print(ex1("I want to eat."))
    # print(ex2("\\d", "Hi, I'm 14 2345", 4))
    # print(ex3("ana are mere 1234 ,,,,,,", ["\\d", ".", "[a-z]+"]))
    # ex6("ceva un cuvant nu stiu ana Ana AnE mare afojeogojigeA")
    # print(ex7("5021018346067"))
    ex8("C:/Users/lucaa/OneDrive/Desktop/Uni/An 3 Sem 1/Python/Lab1","^A|a")
