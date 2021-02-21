'''It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?'''
from math import sqrt


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


primes = get_primes_to(20)
print(primes)


n = 33
cond = True
while(cond == True):
    if not is_prime(n):
        primes = get_primes_to(n)
        # for i in primes:
        count = 0
        while(True):
            i = primes[count]
            if (sqrt((n - i) / 2) == int(sqrt((n - i) / 2))):
                print(n, "=", i, "+ 2* ", int(sqrt((n - i) / 2)), "^2")
                break
            else:
                count += 1
            # else:
            #     print(n, i, sqrt((n - i) / 2))
    n += 2

print(n)
