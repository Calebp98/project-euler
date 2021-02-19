from collections import deque

A = deque([1, 9, 7])

for i in range(len(A)):
    print(A)
    A.rotate()


def is_prime(n):
    if(n<2):
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

circ_primes = []
for i in range(1000000):
    nums = []
    nperms = []
    if(is_prime(i)):
        # print(i)
        val = list(map(int, (str(i))))

        perms = deque(val)


        for _ in range(len(perms)):
            perms.rotate()
            nperms.append(list(perms))
        for num in nperms:
            x = int(''.join(map(str,num)))
            nums.append(x)
        # print(nums)

        if all(is_prime(i) for i in nums):
            circ_primes.append(i)
            print(i)
print(len(circ_primes))
print(circ_primes)
