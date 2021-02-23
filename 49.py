'''The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?'''
from itertools import combinations_with_replacement
from itertools import combinations

from itertools import permutations
from eulerproject import is_prime
from eulerproject import unique_permutations

nums = combinations_with_replacement('0123456789', 4)


def tup_to_int(n):
    return(int(''.join(map(str, n))))


# print(list(nums))

def valid(x):
    return is_prime(tup_to_int(x)) and tup_to_int(x) > 999

def is_arithmetic(l):
    delta = l[1] - l[0]
    for index in range(len(l) - 1):
        if not (l[index + 1] - l[index] == delta):
             return False
    return True
print(is_arithmetic([5, 7, 9, 11]))
print(is_arithmetic([5, 8, 9, 11]))
seqs = [[5, 7, 9, 11],[5, 8, 9, 11]]
for x in seqs:
    # print(x)
    sequence = [list(i) for i in combinations(x,3)]
    # print(sequence)
    for i in sequence:
        if is_arithmetic(i):
            print(i)

prime_tups = []
prime_perms = []
all_prime_perms = []
for tup in nums:
    if sum([valid(x) for x in unique_permutations(tup)]) > 3:
        for x in unique_permutations(tup):
            if valid(x):
                prime_perms.append(tup_to_int(x))
        all_prime_perms.append(prime_perms)
        prime_perms = []
for x in all_prime_perms:
    # print(x)
    sequence = [list(i) for i in combinations(x,3)]
    for i in sequence:
        if is_arithmetic(i):
            print(i)
