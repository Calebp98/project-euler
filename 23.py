'''
*not working not sure why

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.'''

from math import *


def is_abundant(n):
    divisors = []
    divisors.append(1)
    rt = ceil(sqrt(n))
    for i in range(2, ceil(sqrt(n))):
        if(n % i == 0):
            divisors.append(i)
            divisors.append(n / i)
    if((rt**2 == n) and (rt != 1)):
        divisors.append(rt)
    # print(divisors)
    return (sum(divisors) > n)


assert(is_abundant(12) == True)
assert(is_abundant(5) == False)
# assert(is_abundant(1)==False)

limit = 28124

abundant = []
for i in range(limit):
    if (is_abundant(i)):
        abundant.append(i)
        # del abundant[0]
        # print(i)

abundant_sums = []
for i in abundant:
    for j in abundant:
        if ((i + j)<= 28123):
            abundant_sums.append(i + j)
# breakpoint()


nums = [i for i in range(limit)]

not_summable = []
not_summable = (set(nums) - set(abundant_sums))
print(sum(not_summable))
# breakpoint()
