'''An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000'''


# def d(n):
cum = 0
decades = []
n = 10
for dec in range(5):
    n_working = n
    decades.append(dec * 9 * 10**(dec - 1))
    for i in range(len(decades)):
        if(n_working > decades[i]):
            n_working -= decades[i]
            decade = i + 1
print(decades)
print("digit : ",n)
print("dig of dec : ",n_working)
print("decade : ",decade)
num = int(n_working / decade)
print(num)
r_number = int(num)
print("real : ",r_number)
ind = int(decade-num % decade-1)
print(ind)
digit = str(r_number)[ind-1]
print(digit)
