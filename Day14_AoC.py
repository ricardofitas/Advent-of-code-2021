from collections import defaultdict

t, _, *r = open("__21_d14.txt").read().split('\n')
r = dict(r2.split(" -> ") for r2 in r)

p = defaultdict(int)
for a,b in zip(t, t[1:]):
    p[a+b] += 1

def f1(N):
    c2 = defaultdict(int)
    for a in t: c2[a] += 1
    for _ in range(N):
        for (a,b), c in p.copy().items():
            x = r[a+b]
            p[a+b] -= c
            p[a+x] += c
            p[x+b] += c
            c2[x] += c
    return max(c2.values()) - min(c2.values())

# Part 1
print(f1(10))

# Part 2
print(f1(40))