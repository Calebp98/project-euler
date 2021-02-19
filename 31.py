from itertools import combinations_with_replacement

coins = [0.01,0.02,0.05,.1,.2,.5,1,2]
comb = combinations_with_replacement(coins, 200)

for i in list(comb):
    if(sum(i))==1:
        print(list[i])
