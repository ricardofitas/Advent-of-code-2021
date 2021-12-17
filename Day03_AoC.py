

c = open("__21_d03.txt")
lin = c.readlines()

## Part 1
klin = [list([lin[i].split("\n")[0] for i in range(len(lin))][j]) for j in range(len(lin))]
k2 = [1 if [klin[jj][len(klin[0])-ii-1] for jj in range(len(lin))].count('1') > [klin[jj][len(klin[0])-ii-1] for jj in range(len(lin))].count('0') else 0 for ii in range(len(klin[0]))]
prod = sum([k2[ii]*2**ii for ii in range(len(k2))])*sum([abs(k2[ii]-1)*2**ii for ii in range(len(k2))])
print(prod)

## Part 2
ii = 0
klin22 = klin.copy()
while len(klin) > 1:
    klin2 = '1' if [klin[jj][ii] for jj in range(len(klin))].count('1') >= [klin[jj][ii] for jj in range(len(klin))].count('0') else '0'
    klin = [klin[jj] for jj in range(len(klin)) if klin[jj][ii] == klin2]
    ii += 1
k_1 = klin
klin = klin22.copy()
ii = 0
while len(klin) > 1:
    klin3 = '1' if [klin[jj][ii] for jj in range(len(klin))].count('1') < [klin[jj][ii] for jj in range(len(klin))].count(
        '0') else '0'
    klin = [klin[jj] for jj in range(len(klin)) if klin[jj][ii] == klin3]
    ii += 1
k_1 = k_1[0]
k_2 = klin[0]
i3 = sum([int(k_1[ii])*2**(len(k_1)-ii-1) for ii in range(len(k_1))])
j3 = sum([int(k_2[ii])*2**(len(k_2)-ii-1) for ii in range(len(k_2))])
print(i3*j3)
