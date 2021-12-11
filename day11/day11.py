def inside(i,j,n,m):
    return i>=0 and j>=0 and i < n and j < m

def id(i,j,m):
    return (i-1)*m + j

fname = input()
f = open(fname+".txt")
inp = []
for line in f:
    line = list(map(int,line.split('\n')[0]))
    inp.append(line)
res = 0
n = len(inp)
m = len(inp[0])
dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,1,-1]
for step in range(1000):
    nodes = []
    for i in range(n):
        for j in range(m):
            if inp[i][j] == 9:
                nodes.append([i,j])
            inp[i][j]+=1
    while len(nodes) > 0:
        now = nodes[0]
        res += 1
        x = now[0]
        y = now[1]
        nodes = nodes[1:]
        for dir in range(8):
            nowx = x + dx[dir]
            nowy = y + dy[dir]
            if inside(nowx,nowy,n,m):
                if inp[nowx][nowy] == 9:
                    nodes.append([nowx,nowy])
                inp[nowx][nowy]+=1
    tans = 0
    for i in range(n):
        for j in range(m):
            if inp[i][j] > 9:
                inp[i][j] = 0
                tans+=1
    
    if tans == 100:
        print(step+1)
        break
