

c = open("__21_d2.txt")
lin = c.readlines()
dir1 = [i.split(" ")[0] for i in lin]
dir2 = [int(i.split(" ")[1]) for i in lin]

## Part 1
i = sum([dir2[k] for k in range(len(dir2)) if dir1[k] == "forward"])
j = sum([dir2[k] for k in range(len(dir2)) if dir1[k] == "down"]) + sum([-dir2[k] for k in range(len(dir2)) if dir1[k] == "up"])
print(i*j)

## Part 2
aux = [sum([dir2[k] for k in range(k2) if dir1[k] == "down"]) + sum([-dir2[k] for k in range(k2) if dir1[k] == "up"]) for k2 in range(1,len(dir2)+1)]
j = sum([dir2[k]*aux[k] for k in range(len(dir2)) if dir1[k] == "forward"])
print(i*j)
