""""Write two functions to check if a number is prime, and check which of them is more time-efficient."""
import time
from math import sqrt


def prime_func_A(x):
    initial_time = time.time()
    is_prime = True
    if x > 1:
        for i in range(2, int(sqrt(x)) + 1):
            if (x % i) == 0:
                is_prime = False
    if is_prime:
        print(x, "is a prime number.")
    else:
        print(x, "is not a prime number.")
    end_time = time.time()
    return end_time - initial_time


def prime_func_B(x):
    initial_time = time.time()
    is_prime = True
    if x > 1:
        for i in range(2, x // 2):
            if (x % i) == 0:
                is_prime = False
    if is_prime:
        print(x, "is a prime number.")
    else:
        print(x, "is not a prime number.")
    end_time = time.time()
    return end_time - initial_time


if __name__ == '__main__':
    nr = input("Enter number: ")
    time_func_A = prime_func_A(int(nr))
    time_func_B = prime_func_B(int(nr))

    print("Time for A: ", time_func_A,
          "\n Time for B: ", time_func_B)
    if time_func_A < time_func_B:
        print("Function A is faster.")
    else:
        print("Function B is faster.")
