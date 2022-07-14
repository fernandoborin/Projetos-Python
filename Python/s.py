import random

mat = []

for i in range(50):

    l = []

    for j in range(0, 50):

        if(i % 2 == 0):

            l.append(random.randint(0, 50))

        else:
            l.append(random.random())

    mat.append(l)

print(mat)