def is_prime(n):
    if(n<2):
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

assert(is_prime(1)==False)
assert(is_prime(-6)==False)
assert(is_prime(3)==True)
assert(is_prime(4)==False)
assert(is_prime(144)==False)

def is_prime_n_eval(n,a,b):
    return (is_prime(n**2 + a*n + b))

assert(is_prime_n_eval(0,1,41)==True)
assert(is_prime_n_eval(10,1,41)==True)
assert(is_prime_n_eval(41,1,41)==False)


most_consecutive_primes = 0
for a in range(-1000, 1000):
    for b in range(-1000, 1001):
        prime = True
        n = 0
        while(is_prime_n_eval(n,a,b) == True):
            n+=1
        if(n>most_consecutive_primes):
            most_consecutive_primes = n
            answer = a*b
            # print(n)
print(most_consecutive_primes)
print(answer)
