from math import sqrt
from functools import reduce

from itertools import combinations
from itertools import permutations


def is_prime(n):
    if(n < 2):
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def get_primes_to(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    n_prime = []
    for i in range(len(prime)):
        if prime[i]:
            n_prime.append(i)
    return n_prime


def check_pentagonal(p_n):
    n = (sqrt(24 * p_n + 1) + 1) / 6
    return n == int(n)


def check_hexagonal(h_n):
    n = (1 + sqrt(1 + 8 * h_n)) / 4
    return n == int(n)


def factors(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))


def prime_factors(n):

    # Print the number of two's that divide n
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            factors.append(i)
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        factors.append(n)
    return factors


def unique_permutations(iterable, r=None):
    previous = tuple()
    for p in permutations(sorted(iterable), r):
        if p > previous:
            previous = p
            yield p
