def is_prime(number):
    for div in range(2, number):
        if number % div == 0:
            return False
    else:
        return True


def process_item(x):
    """The function will have one parameter, x, and will return the least prime number greater than x. """
    prime_num = x + 1
    while not is_prime(prime_num):
        prime_num += 1
    return prime_num
