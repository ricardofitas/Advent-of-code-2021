c = open('__21_d12.txt')
lin = c.readlines()
inp = [i.split("\n")[0].split("-") for i in lin]

g = {v : {[a, b][a == v] for a, b in inp if v in [a,b]} for v in {w for l in inp for w in l}}
def dfs(v, vis = set(), rep = False, O = True):
    if (rep and v in vis) or v == 'start':
        return 0
    if v == 'end':
        return 1

    return sum(dfs(w, [vis,{*vis,v}][v.islower()], O or v in vis or rep, O) for w in g[v])

#Part 1
S = sum(dfs(v) for v in g['start'])
print(S)

#Part 2
S =sum(dfs(v, O = False) for v in g['start'])
print(S)