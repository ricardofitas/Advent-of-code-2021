import numpy as np

c = open("__21_d06.txt")
lin = c.readlines()

## Part 1
l = lin[0].split("\n")[0].split(",")
l = [int(l[il]) for il in range(len(l))]
T = 80
for k in range(T):
    for il in range(len(l)):
        l[il] -= 1
        if l[il] == -1:
            l[il] = 6
            l.append(8)
print(len(l))

## Part 2
l = lin[0].split("\n")[0].split(",")
l = [int(l[il]) for il in range(len(l))]
T = 256
l2 = [0]*10
for il in l: l2[il+1] += 1

for _ in range(T):
    for i, n in enumerate(l2[1:]):
        l2[i] = n
        l2[i + 1] = 0
    l2[7] += l2[0]
    l2[9] += l2[0]
    l2[0] = 0

print(sum(l2))

