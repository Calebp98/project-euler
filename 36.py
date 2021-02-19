'''The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)'''

total = 0
for i in range(1000001):
    # num = int(str(i)+str(i)[1::-1])
    # print(int(num))
    if str(i) == str(i)[::-1]:
        binary = bin(i)[2:]
        if binary == binary[::-1]:
            total += i
            print(i,binary)
print(total)
