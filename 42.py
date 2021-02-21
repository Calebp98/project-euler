def is_triangle(num):
    triangles = []
    for i in range(1000):
        triangles.append(0.5*i*(i+1))

    if num in triangles:
        return True
    return False

assert(is_triangle(1)==True)
assert(is_triangle(6)==True)
assert(is_triangle(36)==True)
assert(is_triangle(2)==False)
assert(is_triangle(-1)==False)

def fileToList(file):
    names = open(file, 'r')
    names = [line.split(',') for line in names.readlines()][0]
    names = [s.strip('"') for s in names]
    return names

def get_word_value(word):
    total = 0
    for letter in word:
        total += ord(letter)-ord('A')+1
    return total

assert(get_word_value('A')==1)
assert(get_word_value('SKY')==55)


names = fileToList('p042_words.txt')

tri_words = 0
for name in names:
    if is_triangle(get_word_value(name)):
        tri_words += 1
print(tri_words)
