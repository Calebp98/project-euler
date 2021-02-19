triangle ='''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

tri_list = triangle.split('\n')
n = len(tri_list)
triangle_2d_list = []
for i in range(len(tri_list)):
    line = tri_list[i].split()
    line = [int(j) for j in line]
    line.extend([0]*(n-i-1))
    triangle_2d_list.append(line)
en(triangle_2d_list))
print(len(triangle_2d_list[0]))

# Function for finding maximum sum
def maxPathSum(tri, m, n):

    # loop for bottom-up calculation
    for i in range(m-1, -1, -1):
        for j in range(i+1):

            # for each element, check both
            # elements just below the number
            # and below right to the number
            # add the maximum of them to it
            if (tri[i+1][j] > tri[i+1][j+1]):
                tri[i][j] += tri[i+1][j]
            else:
                tri[i][j] += tri[i+1][j+1]

    # return the top element
    # which stores the maximum sum
    return tri[0][0]

# tri = [[1, 0, 0],
# [4, 8, 0],
# [1, 5, 3]]
print(maxPathSum(triangle_2d_list, len(triangle_2d_list)-1, len(triangle_2d_list)-1))
