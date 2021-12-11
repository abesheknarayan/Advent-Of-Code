
fname = input()
inp = []

f = open(fname+".txt")
for line in f :
    line = line.split('\n')[0]
    line = list(map(int,list(line)))
    inp.append(line)
res = 0
n = len(inp)
m = len(inp[0])
val = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        yes = True
        if j < m-1:
            if inp[i][j+1] <= inp[i][j]:
                yes = False
        if j > 0:
            if inp[i][j-1] <= inp[i][j]:
                yes = False
        if yes:
            val[i][j]+=1

for i in range(m):
    for j in range(n):
        yes = True
        if j < n-1:
            if inp[j+1][i] <= inp[j][i]:
                yes = False
        if j > 0:
            if inp[j-1][i] <= inp[j][i]:
                yes = False
        if yes:
            val[j][i]+=1
for i in range(n):
    for j in range(m):
        if val[i][j] == 2:
            res += (inp[i][j]+1)
print(res)