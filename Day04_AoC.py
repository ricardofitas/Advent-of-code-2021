
c = open("__21_d04.txt")
lin = c.readlines()

## Part 1
num_list = list(lin[0].split("\n")[0].split(","))
k = [[[lin[i+g].split("\n")[0].split(" ")[j] for j in range(len(lin[i+g].split("\n")[0].split(" "))) if not lin[i+g].split("\n")[0].split(" ")[j] == ""] for i in range(5)] for g in range(2,len(lin),6)]
h = 0
l = 0
j = [[[0 for kk in range(5)] for jj in range(5)] for ii in range(len(k))]
while l == 0:
    j = [[[1 if k[ii][jj][kk] == num_list[h] or j[ii][jj][kk] == 1 else 0 for kk in range(5)] for jj in range(5)] for ii in range(len(k))]
    for ii in range(len(k)):

        for jj in range(5):
            if all(j[ii][jj]) or all([j[ii][kk][jj] for kk in range(5)]):
                l = 1
                num = sum([sum([int(k[ii][jj2][kk2]) for kk2 in range(5) if j[ii][jj2][kk2] == 0]) for jj2 in range(5)])
                x = num*int(num_list[h])
    h = h + 1
print(x)


## Part 2
num_list = list(lin[0].split("\n")[0].split(","))
k = [[[lin[i+g].split("\n")[0].split(" ")[j] for j in range(len(lin[i+g].split("\n")[0].split(" "))) if not lin[i+g].split("\n")[0].split(" ")[j] == ""] for i in range(5)] for g in range(2,len(lin),6)]
h = 0
j = [[[0 for kk in range(5)] for jj in range(5)] for ii in range(len(k))]
S = []
while not len(S) == len(k):
    j = [[[1 if k[ii][jj][kk] == num_list[h] or j[ii][jj][kk] == 1 else 0 for kk in range(5)] for jj in range(5)] for ii in range(len(k))]
    for ii in range(len(k)):
        if ii not in S:
            for jj in range(5):
                if all(j[ii][jj]) or all([j[ii][kk][jj] for kk in range(5)]):
                    S.append(ii)
                    break
    h = h + 1
ii = S[len(S)-1]
num = sum([sum([int(k[ii][jj2][kk2]) for kk2 in range(5) if j[ii][jj2][kk2] == 0]) for jj2 in range(5)])
x = num*int(num_list[h-1])
print(x)
