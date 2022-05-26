fname = input()
f = open(fname+".txt")
inp = ''
for line in f:
    inp += line
inp = inp.split("\n\n")
alg = inp[0]
newalg = ''
for c in alg:
    if c != '\n':
        newalg += c
alg = newalg
grid = inp[1].split("\n")
n = len(grid)
m = len(grid[0])

offset = 50
emptyLine = ['.' for _ in range(2*offset+m)]

newGrid = []
for _ in range(offset):
    newGrid.append(emptyLine)

print(n,m)

for line in grid:
    nline = []
    for _ in range(offset):
        nline.append('.')
    for x in line:
        nline.append(x)
    for _ in range(offset):
        nline.append('.')
    newGrid.append(nline)

for _ in range(offset):
    newGrid.append(emptyLine)

grid = newGrid

# for line in grid:
#     print(line)

def inside(dx,dy,n,m):
    return dx >= 0 and dy >= 0 and dx < n and dy < m

n = len(grid)
m = len(grid[0])
outputGrid = [['.' for _ in range(m)] for _ in range(n)]

for step in range(50):
    for i in range(n):
        for j in range(m):
            binary = 0
            for dx in range(-1,2):
                for dy in range(-1,2):
                    binary *=2
                    if inside(i+dx,j+dy,n,m):
                        if grid[i+dx][j+dy] == '#':
                            binary +=1
                    else:
                        if step%2 == 1 and alg[0] == '#':
                            binary += 1
            outputGrid[i][j] = alg[binary]
    grid = outputGrid.copy()
    outputGrid = [['.' for _ in range(m)] for _ in range(n)] 
    # for line in grid:
        # print(line)

res = 0
for line in grid:
    for c in line:
        if c == '#':
            res+=1
print(res)
