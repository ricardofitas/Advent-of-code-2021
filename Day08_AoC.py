
c = open("__21_d08.txt")
lin = c.readlines()

## Part 1
l = [i.split("\n")[0].split("| ")[1].split(" ") for i in lin]
c = sum([sum([1 if len(i) in [2, 3, 4, 7] else 0 for i in j]) for j in l])
print(c)

## Part 2
l = [i.split("\n")[0].split(" | ")[0].split(" ") for i in lin]
l1 = [i.split("\n")[0].split(" | ")[1].split(" ") for i in lin]
j2 = [[0, 1, 2, 4, 5, 6], [2, 6], [1, 2, 3, 4, 5], [1, 2, 3, 5, 6], [0, 2, 3, 6], [0, 1, 3, 5, 6], [0, 1, 3, 4, 5, 6],
     [1, 2, 6], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 5, 6]]
S = 0
for ii2, i in enumerate(l):
    ddmat = [['a', 'b', 'c', 'd', 'e', 'f', 'g'] for _ in range(7)]
    pos = 0
    k = 7
    while k > 1:
        j = [[2, 6], [1, 2, 6], [0, 2, 3, 6], [0, 1, 2, 3, 4, 5, 6]]
        for hind,h in enumerate([2, 3, 4, 7]):
            if len(i[pos]) == h:
                inv_lis = [f for f in range(7) if f not in j[hind]]
                for hj in j[hind]:
                    ddmat[hj] = [kk for kk in ddmat[hj] if kk in i[pos]]
                for hj in inv_lis:
                    ddmat[hj] = [kk for kk in ddmat[hj] if kk not in i[pos]]
        j = [[1, 3, 5],[0, 1, 5, 6]]
        for hind, h in enumerate([5, 6]):
            if len(i[pos]) == h:
                for hj in j[hind]:
                    ddmat[hj] = [kk for kk in ddmat[hj] if kk in i[pos]]
        for hj in range(7):
            if len(ddmat[hj]) == 1:
                ddmat = [[kk for kk in ddmat[hj1] if kk not in ddmat[hj]] if hj1 != hj else ddmat[hj] for hj1 in range(7)]
        k = max([len(ddmat[ijk]) for ijk in range(7)])
        pos += 1
    for l3, l2 in enumerate(l1[ii2]):
        h = [[i for i in range(7) if ddmat[i][0] == hj] for hj in l2]
        dig = [f for f in range(10) if all([1 if f2[0] in j2[f] else 0 for f2 in h]) and len(j2[f]) == len(h)][0]
        S += dig * (10**(3-l3))

print(S)
