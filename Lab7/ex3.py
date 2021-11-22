"""" Write a function that will receive as parameters  two strings representing file paths and will return True if
the files are identical or False otherwise. """
import os


def are_identical(filepath1, filepath2):
    if os.path.basename(filepath1) != os.path.basename(filepath2):
        return False;
    else:
        try:
            file1 = open(filepath1, "r")
            file2 = open(filepath2, "r")
        except:
            print("Something went wrong")
        if(file1.read() == file2.read()):
            return True
        else:
            return False


if __name__ == '__main__':
    print(are_identical("C:/Users/lucaa/OneDrive/Desktop/Uni/An 3 Sem 1/Python/Lab7/testDirector/file1.txt",
                  "C:/Users/lucaa/OneDrive/Desktop/Uni/An 3 Sem 1/Python/Lab7/file1.txt"))
