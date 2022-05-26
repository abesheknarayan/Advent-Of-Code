fname = input()
f = open(fname+".txt")
inp = []
for line in f:
    inp.append(line.split("\n")[0])
n = len(inp)
m = len(inp[0])
rightSea = set()
downSea = set()
for i in range(n):
    for j in range(m):
        if inp[i][j] == '>':
            rightSea.add((i,j))
        elif inp[i][j] == 'v':
            downSea.add((i,j))
steps = 0
while True:
    steps+=1
    nowRightSea = set()
    nowDownSea = set()
    filledSea = rightSea | downSea
    moves = 0
    for sea in rightSea:
        xx = sea[0]
        yy = (sea[1]+1)%m
        if filledSea.__contains__((xx,yy)) == False:
            nowRightSea.add((xx,yy))
            moves+=1
        else:
            nowRightSea.add(sea)
    filledSea = nowRightSea | downSea
    for sea in downSea:
        xx = (sea[0]+1)%n
        yy = sea[1]
        if filledSea.__contains__((xx,yy)) == False:
            nowDownSea.add((xx,yy))
            moves+=1
        else:
            nowDownSea.add(sea)
    downSea = nowDownSea
    rightSea = nowRightSea
    if moves == 0:
        break
print(steps)