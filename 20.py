def factorial(n):
    if n ==1:
        return n
    else:
        return n * factorial(n-1)

num = factorial(100)
res = [int(x) for x in str(num)]
print(sum(res))
