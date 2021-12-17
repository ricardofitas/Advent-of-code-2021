import numpy as np

c = open('__21_d17.txt')
lin = c.readlines()

x0 = int(lin[0].split("\n")[0].split("=")[1].split(".")[0])
x1 = int(lin[0].split("\n")[0].split("=")[1].split(".")[-1].split(",")[0])
y0 = int(lin[0].split("\n")[0].split("=")[2].split(".")[0])
y1 = int(lin[0].split("\n")[0].split("=")[2].split(".")[-1])

# Part 1
print(int(abs(y0+1)*(abs(y0+1)+1)/2))

# Part 2
vi = (int(np.sqrt(x0 * 2)), y0)
va = (x1, abs(y0 + 1))

def rt(v):
    p = [0, 0]
    ti = [x0,y0]
    ta = [x1,y1]
    while True:
        for i in range(2): p[i] += v[i]
        v[0] -= 1 if v[0] else 0
        v[1] -= 1
        if p[0] > ta[0] or p[1] < ti[1]: return False
        if all((ti[i] <= p[i] <= ta[i] for i in range(2))): return True

N = sum([sum([1 if rt([i, j]) else 0 for i in range(vi[0], va[0] + 1)]) for j in range(vi[1], va[1] + 1)])
print(N)

