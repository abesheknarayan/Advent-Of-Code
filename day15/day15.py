from queue import PriorityQueue

fname = input()
f = open(fname+".txt")
inp = [] 
for line in f:
    line = line.split("\n")[0]
    line = list(map(int,line))
    inp.append(line)
finp = []
offset = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    for j in range(5):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            offset[i][j] += offset[i][j-1]+1
        else:
            offset[i][j] += offset[i-1][j]+1
for i in range(5):
    temp = []
    for line in inp:
        for j in range(5):
            for x in line:
                val = x + offset[i][j]
                if val >= 10:
                    val-=9
                temp.append(val)
        finp.append(temp)
        temp = []

inp = finp
n = len(inp)
inf = 10**9
q = PriorityQueue()
dp = [[inf for _ in range(n)] for _ in range(n)]
dp[0][0] = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def inside(x,y,n):
    return x>=0 and y>=0 and x < n and y < n 

q.put([0,0,0])
while not q.empty():
    top = q.get()
    x = top[1]
    y = top[2]
    dis = top[0]
    for i in range(4):
        nowx = x + dx[i]
        nowy = y + dy[i]
        if inside(nowx,nowy,n):
            if dp[nowx][nowy] > dis + inp[nowx][nowy]:
                dp[nowx][nowy] = dis + inp[nowx][nowy]
                q.put([dp[nowx][nowy],nowx,nowy])
print(dp[n-1][n-1])


