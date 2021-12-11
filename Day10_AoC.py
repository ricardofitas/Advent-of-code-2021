import time
import numpy as np

c = open("__21_d10.txt")
lin = c.readlines()

l = [i.split("\n")[0] for i in lin]
s = [3, 57, 1197, 25137]
p = [")", "]", "}", ">"]
q = ["(", "[", "{", "<"]

## Part 1
S = 0
logt = 0
for ii,k in enumerate(l):
    sc = []
    for k2 in k:
        if k2 not in p:
            sc += [k2]
        else:
            for xind, x in enumerate(p):
                if k2 in x:
                    if q[xind] not in sc[len(sc)-1]:
                        S += s[xind]
                        logt = 1
                    else:
                        sc = sc[:(len(sc) - 1)]
        if logt == 1:
            logt = 0
            break
print(S)

## Part 2
S = []
logt = 0
for ii,k in enumerate(l):

    sc = []
    for k2 in k:
        if k2 not in p:
            sc += [k2]
        else:
            for xind, x in enumerate(p):
                if k2 in x:
                    if q[xind] not in sc[len(sc)-1]:
                        logt = 1
                    else:
                        sc = sc[:(len(sc) - 1)]
        if logt == 1:
            break
    if logt == 1:
        logt = 0
    else:
        S += [0]
        for hh in sc[::-1]:
            for xind, x in enumerate(q):
                if hh in x:
                    S[len(S)-1] = S[len(S)-1] * 5 + xind + 1

Sf = int(np.median(S))
print(Sf)