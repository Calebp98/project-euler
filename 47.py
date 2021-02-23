'''The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?'''

import eulerproject

# while(True):
i = 12
factors = eulerproject.prime_factors(i)

n = 1
cond = True
while cond:
    if len(set(eulerproject.prime_factors(n))) == 4:
        n += 1
        if len(set(eulerproject.prime_factors(n))) == 4:
            n += 1
            if len(set(eulerproject.prime_factors(n))) == 4:
                n += 1
                if len(set(eulerproject.prime_factors(n))) == 4:
                    print(n - 3)
                    print(set(eulerproject.prime_factors(n - 3)))
                    print(set(eulerproject.prime_factors(n - 2)))
                    print(set(eulerproject.prime_factors(n - 1)))
                    print(set(eulerproject.prime_factors(n)))
                    cond = False
    else:
        n += 1
