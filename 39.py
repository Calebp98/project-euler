'''If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?'''

import itertools

def partitions(n, k):
    for c in itertools.combinations(range(n+k-1), k-1):
        yield [b-a-1 for a, b in zip((-1,)+c, c+(n+k-1,))]

# Example usage
def get_triangles(n):
    triangles = []
    for p in partitions(n-3, 3):
        p = [x+1 for x in p]
        if(p[0]**2==p[1]**2+p[2]**2):
            triangles.append(p)
    triangles = triangles[::2]
    return triangles

# print(get_triangles(120))
# print(get_triangles(4))

tris = []
i_tris = 0
for i in range(1001):
    if i%100==0:
        print(i)
    n_tris = get_triangles(i)
    if len(tris) < len(n_tris):
        tris = n_tris
        i_tris = i
print(i_tris)
