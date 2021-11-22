import random
import time

"""" Write a program that will write the minutes passed from the start, every x seconds, where x is random chosen at
each iteraton (from the inteval [a, b] , where a, b are arguments). The program will run infinitely. """

if __name__ == '__main__':
    a = input("Enter a from the interval [a,b]: ")
    b = input("Enter b from the interval [a,b]: ")
    print(a, b)
    while True:
        x = random.randint(int(a), int(b))
        print(x)
        time.sleep(x - 1)
        print("Minute: ", time.strftime("%M"))
