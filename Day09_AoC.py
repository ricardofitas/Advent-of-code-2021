import numpy as np

c = open("__21_d09.txt")
#c = open("12.txt")
lin = c.readlines()

l = [i.split("\n")[0] for i in lin]
l = [[int(j) for j in i] for i in l]
k = [[[1]+[1 if l[k][i]<l[k][i-1] else 0 for i in range(1,len(l[k]))] for k in range(len(l))]]
k = k+[[[1 if l[k][i]<l[k][i+1] else 0 for i in range(len(l[k])-1)]+[1] for k in range(len(l))]]
k = k+[[[1]*len(l[0])] + [[1 if l[k][i]<l[k-1][i] else 0 for i in range(len(l[k]))] for k in range(1,len(l))]]
k = k+[[[1 if l[k][i]<l[k+1][i] else 0 for i in range(len(l[k]))] for k in range(len(l)-1)] + [[1]*len(l[0])]]
S = int(sum([sum([np.floor(sum([k[i3][i1][i2] for i3 in range(4)])/4)*(l[i1][i2]+1) for i2 in range(len(l[0]))]) for i1 in range(len(l))]))
print(S)
quit()


for y, line in enumerate(lin):
    for x, char in enumerate(line.strip()):
        map[(x, y)] = int(char)
def get_neighbours(x, y):
    return {(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)}
def is_low_point(x, y):
    return all(map.get(pos, 9) > map[(x, y)] for pos in get_neighbours(x, y))
def get_low_points():
    return [(x, y) for x, y in map if is_low_point(x, y)]
print("Part 1:")
print(sum(map[pos] + 1 for pos in get_low_points()))

def get_basin(pos):
    basin = {pos}
    follow(pos, basin)
    return basin
def follow(pos, basin):
    x, y = pos
    p1 = map[pos]
    for neighbour in get_neighbours(x, y):
        p2 = map.get(neighbour, 0)
        if p2 > p1 and p2 != 9:
            basin.add(neighbour)
            follow(neighbour, basin)
p = 1
for x in sorted(len(get_basin(pos)) for pos in get_low_points())[-3:]:
    p *= x

print("Part 2:")
print(p)