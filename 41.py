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

n = 100

# for i in range(1,n+1):
i = 7
digits = [x+1 for x in range(i)]
# print(digits)
pandigitals = list(permutations(digits,i))
pandigitals = [int(''.join(map(str, x)))  for x in pandigitals]
# print(pandigitals)
for num in pandigitals:
    if is_prime(num): print(num)
