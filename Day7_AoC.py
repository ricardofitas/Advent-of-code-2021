import numpy as np

c = open("__21_d07.txt")
lin = c.readlines()

## Part 1
l = [int(i) for i in lin[0].split("\n")[0].split(",")]
lm = np.median(l)
print(sum([abs(i-lm) for i in l]))

## Part 2
llm1 = [abs(i - np.floor(np.mean(l))) for i in l]
llm2 = [abs(i - np.ceil(np.mean(l))) for i in l]
lt = min(sum([(i*(i+1))/2 for i in llm1]),sum([(i*(i+1))/2 for i in llm2]))
print(lt)