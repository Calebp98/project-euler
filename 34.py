from math import factorial



for i in range(1000000):
    total=0
    val = list(map(int, (list(str(i)))))
# print(vals)
    for digit in val:
        total+=factorial(digit)
    if total == i:
        print(i)
