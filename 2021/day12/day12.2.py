res = 0
def go(x,st,des,adj,vis,spe,node):
    global res
    if spe.__contains__(x) == False:
        vis[x] += 1
    if x == des:
        res +=1
    else:
        for it in adj[x]:
            if it == node:
                if vis[it] < 2:
                    go(it,st,des,adj,vis,spe,node)
            elif vis[it] == 0:
                go(it,st,des,adj,vis,spe,node)
        
    if spe.__contains__(x) == False:
        vis[x] -= 1
fname = input()
f = open(fname+".txt")
nodes = set()
inp = []
for line in f:
    line = line.split("\n")[0]
    line = line.split('-')
    inp.append([line[0],line[1]])
    nodes.add(line[0])
    nodes.add(line[1])
n = len(nodes)
mapping = {}
revmap = {}
no = 0
for node in nodes:
    mapping[node] = no
    revmap[no] = node
    no+=1
spe = set()
st = mapping['start']
en = mapping['end']
smallCaves = set()
for node in nodes:
    if node.isupper():
        spe.add(mapping[node])
    else :
        if node == 'start' or node == 'end':
            continue
        else:
            smallCaves.add(mapping[node])
m = len(inp)
adj = [[] for _ in range(n)]
for edg in inp:
    x = mapping[edg[0]]
    y = mapping[edg[1]]
    adj[x].append(y)
    adj[y].append(x)
vis = [0 for _ in range(n)]
go(st,st,en,adj,vis,spe,-1)
oldres = res
res = 0
for node in smallCaves:
    path = []
    go(st,st,en,adj,vis,spe,node)
print(res-oldres*(len(smallCaves)-1))