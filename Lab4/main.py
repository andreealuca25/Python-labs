import glob
import os
from os.path import isfile, join


def ex1(path):
    # 1)Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.
    # Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din
    # directorul dat ca parametru. Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’

    only_files = [f for f in os.listdir(path) if isfile(join(path, f))]  # keeps only the files from the pathname
    only_files = [os.path.splitext(x)[1] for x in only_files]
    only_files = [x[1:] for x in only_files]  # removes the '.' from the extension

    only_files.sort()
    return only_files


def ex2(dir_path, file):
    # 2)	Să se scrie o funcție ce primește ca argumente două căi: director si fișier.
    # Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie,
    # calea absolută a fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A.
    only_files = [f for f in os.listdir(dir_path) if isfile(join(dir_path, f))]
    only_files = [x for x in only_files if x[0] == 'A']

    only_files = [os.path.abspath(x) for x in only_files]

    f = open(file, "a")
    for file_path in only_files:
        f.write(file_path + "\n")
    f.close()


def ex3(my_path):
    # 3)Să se scrie o funcție ce primește ca parametru un string my_path. Dacă parametrul reprezintă calea către un
    # fișier, se vor returna ultimele 20 de caractere din conținutul fișierului. Dacă parametrul reprezintă calea
    # către un director, se va returna o listă de tuple (extensie, count), sortată descrescător după count,
    # unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu acea extensie. Lista se obține
    # din toate fișierele (recursiv) din directorul dat ca parametru.
    if os.path.isdir(my_path):
        files_dict = dict()
        for filename in glob.iglob(my_path + '**/**', recursive=True):
            key = os.path.splitext(filename)[1]
            if key in files_dict:
                files_dict[key] += 1
            else:
                files_dict.update({key: 1})

        # converting dict into list of tuple
        files_list = [(k, v) for k, v in files_dict.items()]
        files_list.sort(key=lambda x: x[1], reverse=True)
        return files_list

    elif os.path.isfile(my_path):
        file = open(my_path, "r")
        data = file.read()
        nr_of_chars = len(data)
        return data[nr_of_chars - 20:nr_of_chars]


def ex4(my_path):
    # 4)	Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca
    # argument la linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.

    only_files = [f for f in os.listdir(my_path) if isfile(join(my_path, f))]  # keeps only the files from the pathname
    only_files = [os.path.splitext(x)[1] for x in only_files]

    set_files = set(only_files)
    list_files = list(set_files)
    list_files.sort()

    return list_files


def ex5(target, to_search):
    # 5)	Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și
    # returneaza o listă de fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este un fișier,
    # se caută doar in fișierul respectiv iar dacă este un director se va căuta recursiv in toate fișierele din acel
    # director. Dacă target nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError cu un
    # mesaj corespunzator.
    if os.path.isdir(target):
        for filename in glob.iglob(target + '**/*.txt', recursive=True):
            try:
                with open(filename) as file:
                    if to_search in file.read():
                        return True
            except IOError:
                print("Eroare cu deschiderea / inchiderea fisierului")
        return False

    elif os.path.isfile(target):
        with open(target) as file:
            if to_search in file.read():
                return True
        return False
    else:
        raise ValueError('Target nu e nici file, nici director.')


def callback():
    pass


def ex6(target, to_search, callback):
    # https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
    pass


if __name__ == '__main__':
    # print(ex1("."))
    # ex2(".", "./test.txt")
    # print(ex3("C:/Users/lucaa/OneDrive/Desktop/Uni/An 3 Sem 1/Python/Lab1"))
    # print(ex4("C:/Users/lucaa/OneDrive/Desktop/Uni/An 3 Sem 1/Python/Lab1"))
    print(ex5("C:/Users/lucaa/OneDrive/Desktop/Uni/An 3 Sem 1/Python/Lab1", "ce caut aici"))
