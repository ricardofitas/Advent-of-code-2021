
c = open("__21_d01.txt")
lin = c.readlines()
lines_stn = [int(i.split("\n")[0]) for i in lin]

## Part 1
c = [(lines_stn[i-1]-lines_stn[i])<0 for i in range(1,len(lines_stn))]
print(c.count(True))

## Part 2
c = [(sum(lines_stn[(i-3):i])-sum(lines_stn[(i-2):(i+1)]))<0 for i in range(3,len(lines_stn))]
print(c.count(True))
