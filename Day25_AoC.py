import numpy as np

lin = open("__21_d25.txt").read().splitlines(); gm = np.array([list(line) for line in lin])

def st(hN, gm):
	tM = gm == hN; gS = np.roll(gm, -1, 1 if hN == ">" else 0)
	tM[gS != '.'] = False;	gm[tM] = '.'; tS = np.roll(tM, 1, 1 if hN == ">" else 0)
	gm[tS] = hN; return len(gm[tM])

count = 1
while st('>', gm) + st('v', gm) > 0: count += 1
print(count)