
c = open("__21_d05.txt")
lin = c.readlines()

## Part 1

def point_array(x1,y1,x2,y2):
    if x1 == x2:
        if y1 < y2:
            return [[x1,f] for f in range(y1,y2+1)]
        else:
            return [[x1, f] for f in range(y2, y1 + 1)]
    if y1 == y2:
        if y1 == y2:
            if x1 < x2:
                return [[f,y1] for f in range(x1,x2+1)]
            else:
                return [[f,y1] for f in range(x2,x1+1)]
    if not (x1 == x2 or y1 == y2):
        m = int((y2-y1)/(x2-x1))
        b = y2-x2*m
        if x1 < x2:
            return [[f, m*f + b] for f in range(x1, x2 + 1)]
        else:
            return [[f, m*f + b] for f in range(x2, x1 + 1)]

k = [[lin[i].split("\n")[0].split(" -> ")[j].split(",") for j in range(2)] for i in range(len(lin))]
a = [point_array(int(k[i][0][0]),int(k[i][0][1]),int(k[i][1][0]),int(k[i][1][1])) for i in range(len(lin))]
m = [max([max([a[i][j][k] for j in range(len(a[i]))]) for i in range(len(a))]) for k in range(2)]
lista_final = [[0 for _ in range(m[1]+1)] for _ in range(m[0]+1)]
for i in range(len(a)):
    for j in range(len(a[i])):
        lista_final[a[i][j][0]][a[i][j][1]] += 1

res = sum([sum([1 if lista_final[i][j]>1 else 0 for j in range(len(lista_final[i]))]) for i in range(len(lista_final))])

print(res)