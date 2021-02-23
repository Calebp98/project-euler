last_total = 0
total = 0
last_digits = 10
for i in range(1, 1001):
    L = str(i**i)
    last_total += int(L[- last_digits:])
    last_total = int(str(last_total)[- last_digits:])
print(i, last_total)
