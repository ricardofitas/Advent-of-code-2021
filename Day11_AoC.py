
# Day 11 Advent of Code 2021
# Change txt name in line 34

def do_step(l,S):
    log = True if any([any([1 if j2 == 10 else 0 for j2 in j]) for j in l]) else False
    while log:
        for jind,j in enumerate(l):
            for j2ind,j2 in enumerate(j):
                if j2 == 10:
                    if jind != 0:
                        if j2ind != 0:
                            l[jind-1][(j2ind-1)] += 1 if l[jind-1][(j2ind-1)] not in [0,10] else 0
                        l[jind-1][j2ind] += 1 if l[jind-1][j2ind] not in [0,10] else 0
                        if j2ind != len(j)-1:
                            l[jind-1][j2ind+1] += 1 if l[jind-1][j2ind+1] not in [0,10] else 0
                    if j2ind != 0:
                        l[jind][(j2ind - 1)] += 1 if l[jind][(j2ind - 1)] not in [0,10] else 0
                    if j2ind != len(j)-1:
                        l[jind][(j2ind + 1)] += 1 if l[jind][(j2ind + 1)] not in [0,10] else 0
                    if jind != len(l)-1:
                        if j2ind != 0:
                            l[jind+1][(j2ind-1)] += 1 if l[jind+1][(j2ind-1)] not in [0,10] else 0
                        l[jind+1][j2ind] += 1 if l[jind+1][j2ind] not in [0,10] else 0
                        if j2ind != len(j)-1:
                            l[jind+1][j2ind+1] += 1 if l[jind+1][j2ind+1] not in [0,10] else 0

                    l[jind][j2ind] = 0
                    S += 1
        log = True if any([any([1 if j2 == 10 else 0 for j2 in j]) for j in l]) else False

    return l, S

c = open("__21_d11.txt")
lin = c.readlines()

l = [i.split("\n")[0] for i in lin]
l = [[int(j2) for j2 in j] for j in l]
l2 = l.copy()

#Part 1
T = 100
S = 0
for _ in range(T):
    l = [[j2 + 1 for j2 in j] for j in l]
    [l,S] = do_step(l,S)
print(S)

#Part 2
S = 0
log2 = True
iT = 0
l = l2.copy()
while log2:
    l = [[j2 + 1 for j2 in j] for j in l]
    [l,S] = do_step(l,S)
    iT += 1
    if all([all([1 if j2 == 0 else 0 for j2 in j]) for j in l]) == 1:
        log2 = False
print(iT)
