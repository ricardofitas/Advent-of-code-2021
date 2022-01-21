c = open("__21_d24.txt")
b = [b.split('\n') for b in c.read().split('inp w\n')[1:]]
mma = [0] * 14; mmi = [0] * 14; st = []

for i, bl in enumerate(b):
  if bl[3] == 'div z 1': st.append((i, int(bl[14].split(' ')[-1])))
  elif bl[3] == 'div z 26':
    j, x = st.pop(); dd = x + int(bl[4].split(' ')[-1])
    if dd < 0: i, j, dd = j, i, -dd
    mma[i] = 9; mma[j] = 9 - dd; mmi[i] = 1 + dd;   mmi[j] = 1


p1 = ''.join(map(str, mma)); print(p1) #Part 1
p2 = ''.join(map(str, mmi)); print(p2) #Part 2