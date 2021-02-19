'''Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''
import math


def d(n):
    total = 0
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if(n % i == 0):
            total += i
            total += n / i
    return total - n


def is_amicable(a, b):
    if((d(a) == b) and (d(b) == a)):
        return True
    else :
        return False

assert(d(220) == 284)
assert(is_amicable(220,284)==True)
assert(is_amicable(220,283)==False)

total=0
for i in range(1,10000):
    if((d(d(i))==i) and (d(i)!=i)):
        total+=i
        print(i)
print(total)
