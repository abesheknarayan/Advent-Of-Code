def inside(i,j,n,m):
    return i>=0 and j>=0 and i < n and j < m

def id(i,j,m):
    return (i-1)*(m) + j
def dfs(x,adj,vis):
    vis[x] = True
    res = 1
    for xx in adj[x]:
        if vis[xx] == True:
            continue
        
        res += dfs(xx,adj,vis)
    return res
fname = input()
f = open(fname+".txt")
inp = []
for line in f :
    line = line.split('\n')[0]
    line = list(map(int,list(line)))
    inp.append(line)
n = len(inp)
m = len(inp[0])
adj = [{} for _ in range(n*m)]
node = [[0 for _ in range(m)] for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(n):
    for j in range(m):
        if inp[i][j] != 9:
            node[i][j] = 1
for i in range(n):
    for j in range(m):
        if node[i][j] == 0:
            continue
        for dir in range(4):
            nowx = dx[dir] + i
            nowy = dy[dir] + j
            if inside(nowx,nowy,n,m):
                if node[nowx][nowy] == 1:
                    adj[id(i,j,m)][(id(nowx,nowy,m))]=1
vis = [False for _ in range(n*m)]
res = []
for i in range(n):
    for j in range(m):
        if node[i][j] == 0:
            continue
        if vis[id(i,j,m)] == False:
            comp = 0
            tans = dfs(id(i,j,m),adj,vis)
            res.append(tans)

res.sort()
print(res[-1]*res[-2]*res[-3])
