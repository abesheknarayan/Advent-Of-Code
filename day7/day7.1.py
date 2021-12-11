fname = input()
f = open(fname+".txt")
pos = list(map(int,f.readline().split(',')))
res = 10**9
for i in range(min(pos),max(pos)+1):
    tans = 0
    for j in pos:
        no = abs(i-j)
        tans += (no*(no+1))//2
    res = min(res,tans)
print(res)