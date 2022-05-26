def mark(line,freq):
    x1 = line[0][0]
    x2 = line[1][0]
    y1 = line[0][1]
    y2 = line[1][1]
    if x1 == x2:
        for i in range(min(y1,y2),max(y1,y2)+1):
            freq[i][x1]+=1
    if y1 == y2 and x1 != x2:
        for i in range(min(x1,x2),max(x1,x2)+1):
            freq[y1][i]+=1
    difx = abs(x1-x2)
    dify = abs(y1-y2)
    if difx == dify:
        minx = min(x1,x2)
        sx = minx 
        ex = -1
        sy = -1
        ey = -1
        if x1 == minx:
            sy = y1
            ex = x2
            ey = y2
        else:
            sy = y2
            ex = x1
            ey = y1
        if sy > ey:
            step = [1,-1]

        else :
            step = [1,1]
        point = [sx,sy]
        for i in range(sx,ex+1):
            xx = point[0]
            yy = point[1]
            freq[yy][xx] += 1
            point[0] += step[0]
            point[1] += step[1]

        
fname = input()
f = open(fname+".txt")
lines = []
maxx = 0
maxy = 0
for x in f:
    inp = x.split('\n')[0]
    inp = inp.split(" -> ")
    left = list(map(int,inp[0].split(',')))
    right = list(map(int,inp[1].split(',')))
    maxx = max(maxx,left[0],right[0])
    maxy = max(maxy,left[1],right[1])
    lines.append([left,right])
n = len(lines)
freq = [[0 for i in range(maxy+1)]for j in range(maxx+1)]
for line in lines:
    mark(line,freq)

res = 0

for x in freq:
    for xx in x:
        if xx >=2:
            res +=1

print(res)