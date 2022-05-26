# let x,xi be the x-coordinates of scanner 0 and i.
# pts[i] is list of all points for scanner i.
# foundPts is a set of all distinct points in ref of (0,0,0) in direction (1,1,1)
# first loop through foundPts and pts[i] and take 2 pairs of points as the same for now
# then for all permutation and [+-1,+-1,+-1] directions we can calculate (x1,y1,z1)
# with that as ref now we should deref points into (0,0,0) pov and check if there is 11 more points matching
# if yes then we can take the coords of xi as perm(x1,y1,z1)*(directionVector(+-1,+-1,+-1))
# add all these points to foundPts and continue the same with remaining points


from itertools import permutations

# returns the point after resolving permutation and direction vectors
def getPoint(pt,perm,dir):
    newpt = pt.copy()
    for i in range(3):
        newpt[i] = pt[perm[i]-1]*dir[i]
    return newpt        

def subtractPoint(pt1,pt2):
    newpt = pt1.copy()
    for i in range(3):
        newpt[i] -= pt2[i]
    return newpt

def addPoint(pt1,pt2):
    newpt = pt1.copy()
    for i in range(3):
        newpt[i] += pt2[i]
    return newpt


def compute(indx0,indx1,inp,found,bfound,foundPts):
    permlist = list(permutations(range(1,4)))
    for pt1 in inp[indx0]:
        for pt2 in inp[indx1]:
            for perm in permlist:
                for di in range(-1,2,2):
                    for dj in range(-1,2,2):
                        for dk in range(-1,2,2):
                            newpt2 = getPoint(pt2,perm,[di,dj,dk])
                            scanner2 = subtractPoint(pt1,newpt2)
                            matching = 1
                            unmatchingPts = []
                            newinp = []
                            for pt3 in inp[indx1]:
                                newpt3 = getPoint(pt3,perm,[di,dj,dk])
                                realPt3 = addPoint(newpt3,scanner2)
                                newinp.append(realPt3)
                                if pt3 == pt2:
                                    continue
                                if inp[indx0].__contains__(realPt3) == True:
                                    matching += 1
                                else:
                                    unmatchingPts.append(realPt3)
                            if matching >= 12:
                                inp[indx1] = newinp
                                for pts in unmatchingPts:
                                    foundPts.add(tuple(pts))  
                                found[indx1] = scanner2
                                bfound[indx1] = True
                                return

fname = input()
f = open(fname+".txt")
inp = []
temp = []
for line in f:
    if line == '\n':
        inp.append(temp)
        temp = []
        continue
    if line.__contains__("scanner"):
        ...
    else: 
        line = list(map(int,line.split('\n')[0].split(',')))
        temp.append(line)
inp.append(temp)
temp = []
n = len(inp)
print(n)
found = [ [] for _ in range(n)] # [x,y,z]
bfound = [False for _ in range(n)]
found[0] = [0,0,0]
bfound[0] = True
foundPts = set()
for pt in inp[0]:
    foundPts.add(tuple(pt))
q = []
q.append(0)
while len(q) > 0:
    print(q)
    indx = q.pop()
    for i in range(n):
        if i == indx:
            continue
        if bfound[i] == False:
            compute(indx,i,inp,found,bfound,foundPts)
            if bfound[i] == True:
                q.append(i)
print(len(foundPts))

## part 2

def getManhattanDistance(pt1,pt2):
    res = 0
    for i in range(3):
        res += abs(pt1[i]-pt2[i])
    return res

maxManhattanDistance = 0
for i in range(n):
    for j in range(n):
        maxManhattanDistance = max(maxManhattanDistance,getManhattanDistance(found[i],found[j]))

print(maxManhattanDistance)
