size = 1001
ru = 0
rd = 0
lu = 0
ld = 0
total=1
for i in range(2,size+1):
    if((i+1)%2==0):
        ru = i**2
        lu = ru - (i-1)
        ld = lu - (i-1)
        rd = ld - (i-1)
        print(i,ru,lu,ld,rd)
        total += ru+lu+ld+rd
print(total)
