def ex1(a, b):
    inter_a_b = [x for x in a if x in b]
    a_minus_b = [x for x in a if x not in b]
    b_minus_a = [x for x in b if x not in a]
    reunion_a_b = a + b

    inter_a_b_set = set(inter_a_b)
    a_minus_b_set = set(a_minus_b)
    b_minus_a_set = set(b_minus_a)
    reunion_a_b_set = set(reunion_a_b)

    list_of_sets = list()
    list_of_sets.append(inter_a_b_set)
    list_of_sets.append(a_minus_b_set)
    list_of_sets.append(b_minus_a_set)
    list_of_sets.append(reunion_a_b_set)

    return list_of_sets


def ex2(my_str):
    dictionary = {

    }

    for character in my_str:
        key = character
        if 'a' <= character <= 'z' or 'A' <= character <= 'Z':
            if key in dictionary:
                dictionary[key] += 1
            else:
                dictionary.update({key: 1})

    return dictionary


def ex4_build_xml_element(tag, content, href, class1, idd):
    result = "<" + tag + " href=\"" + href + \
             "\" _class=\"" + class1 + "\" id=\"" + \
             idd + "\">" + content + "</" + tag + ">"

    return result


def ex5(rules, dictionary):
    print(dictionary.keys())
    for rule in rules:
        if rule not in dictionary.keys():
            return False
    for rule in rules:
        word = rule[1] + rule[2] + rule[3]
        flag_word = False
        if word in dictionary.values():
            flag_word = True
        if not flag_word:
            return False
    return True


def ex6(elem_list):
    elem_set = set()
    for elem in elem_list:
        elem_set.add(elem)

    return len(elem_set), len(elem_list) - len(elem_set)


if __name__ == '__main__':
    print("lab3")
    # 1.Write a function that receives as parameters two lists a and b and returns a list of sets containing:
    # (a intersected with b, a reunited with b, a - b, b - a)

    # list_a, list_b = [1, 2, 3, 4, 5], [3, 6, 7, 8]
    #
    # print(ex1(list_a, list_b))

    # 2.Write a function that receives a string as a parameter and returns a dictionary
    # in which the keys are the characters in the character string and
    # the values are the number of occurrences of that character in the given text.

    # input_str = input("Enter a string: ")
    # print(ex2(input_str))

    # 4. The build_xml_element function receives the following parameters: tag, content,
    # and key-value elements given as name-parameters.
    # Build and return a string that represents the corresponding XML element.
    # Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " some ")
    # returns  the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"

    # print(ex4_build_xml_element("a", "Hello there", "http://python.org", "my-link", "some"))

    # 5.The validate_dict function that receives as a parameter a set of tuples
    # ( that represents validation rules for a dictionary that has strings as keys and values) and a dictionary.
    # A rule is defined as follows: (key, "prefix", "middle", "suffix").
    # A value is considered valid if it starts with "prefix", "middle"
    # is inside the value (not at the beginning or end) and ends with "suffix".
    # The function will return True if the given dictionary matches all the rules, False otherwise.

    # Example: the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    # and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
    # => False because although the rules are respected for "key1"
    # and "key2" "key3" that does not appear in the rules.

    # s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    # d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}

    # print(ex5(s, d))

    # 6. Write a function that receives as a parameter a list and returns a tuple (a, b),
    # representing the number of unique elements in the list,
    # and b representing the number of duplicate elements in the list (use sets to achieve this objective).

    # print(ex6([1, 2, 3, 1, 4, 1, 3]))

    # 7. pe git https://github.com/jesusjimsa/Python-Programming-UAIC/blob/master/Lab%203/ex9.py

    # 8. 8. Write a function that receives a single dict parameter named mapping. This dictionary always contains a
    # string key "start". Starting with the value of this key you must obtain a list of objects by iterating over
    # mapping in the following way: the value of the current key is the key for the next value, until you find a loop
    # (a key that was visited before). The function must return the list of objects obtained as previously described.
    #
    # Ex: loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
    # will return ['a', '6', 'z', '2']
    # hai pa, sincer

