
# Part 1
p1 = False
G = {}
for lin in open("__21_d13.txt"):
    lin = lin.strip()
    if lin and lin.startswith('fold'):
        G2 = {}
        instr = lin.split()[-1]
        d,v = instr.split('=')
        v = int(v)
        if d == 'x':
            for (x,y) in G:
                if x < v:
                    G2[(x,y)] = True
                else:
                    G2[(v-(x-v), y)] = True
        else:
            assert d == 'y'
            for (x,y) in G:
                if y < v:
                    G2[(x,y)] = True
                else:
                    G2[(x, v-(y-v))] = True
        G = G2
        if not p1:
            p1 = True
            print(len(G2))
    elif lin:
        x,y = [int(v) for v in lin.strip().split(',')]
        G[(x,y)] = True

X = max([x for x,y in G.keys()])
Y = max([y for x,y in G.keys()])

# Part 2
ans = ''
for y in range(Y+1):
    for x in range(X+1):
        ans += ('x' if (x,y) in G else ' ')
    print(ans)
    ans = ''