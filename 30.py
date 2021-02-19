power = 5

total=0
for i in range (10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        res = int("".join(map(str, [i,j,k,l,m,n])))
                        if(res == (i**power+j**power+k**power+l**power+m**power+n**power)):
                            total += res
print(total-1)
