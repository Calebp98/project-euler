'''The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.'''
from itertools import product


def permutations_with_replacement(n, m):
    for i in product(list(range(1, m + 1)), repeat=n):
        yield i


def is_prime(n):
    if(n < 2):
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def is_trunc(n):
    n = str(n)
    if len(n)<2:
        return False
    cond = True
    for i in range(len(n)):
        if not is_prime(int(n[i:])):
            cond = False
        if n[:i]!='':
            if not is_prime(int(n[:i])):
                cond = False
    return cond



print(is_trunc(3797))
print(is_trunc(12))
print(is_trunc(31))



units = [1, 2, 3, 5, 7,9]
nums = []
truncs = []
total = 0
a = 7

for n in range(a):
    perms = permutations_with_replacement(n, 6)
    perms = list(perms)
    perms = [list(x) for x in perms]
    # print(perms[0])
    for ind in perms:
        # print(ind)
        num = []
        for i in ind:
            num.append(units[i - 1])
        str_num = [str(x) for x in num]
        num = ""
        for i in str_num:
            num += i
        # print(num)
        if num != '':
            num = int(num)
            nums.append(num)
    for i in nums:
        if i not in truncs:
            if is_trunc(i):
                truncs.append(i)
print(i)
total = sum(truncs)
print(truncs)
print(len(truncs))
print(total)
