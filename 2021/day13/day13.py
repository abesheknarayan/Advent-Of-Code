fname = input()
f = open(fname+".txt")
pts = []
folds = []
for line in f:
    if line == '\n':
        continue 
    line = line.split("\n")[0]
    line = line.split(" ")
    if line[0] == "fold":
        # fold instruction
        command = line[2].split("=")
        axis = 0
        if command[0] == 'y':
            axis = 1
        folds.append([axis,int(command[1])])
    else:
        line = line[0].split(",")
        pts.append([int(line[0]),int(line[1])])

def fold(command,pts):
    res = []
    if command[0] == 0:
        ref = command[1]
        maxx = 0
        for pt in pts:
            maxx = max(maxx,abs(pt[0]-ref))
        for pt in pts:
            res.append([maxx-abs(pt[0]-ref),pt[1]])
    else:
        ref = command[1]
        maxy = 0
        for pt in pts:
            maxy = max(maxy,abs(pt[1]-ref))
        for pt in pts:
            res.append([pt[0],maxy-(abs(pt[1]-ref))])
    return res

def hash(pt):
    return str(pt[0]) + '$' + str(pt[1])     

def distinct(pts):
    m = set()
    for pt in pts:
        m.add(hash(pt))
    return len(m)
for fo in folds:
    pts = fold(fo,pts)


def draw(pts):
    maxx = 0
    maxy = 0
    for pt in pts:
        maxx = max(maxx,pt[0])
        maxy = max(maxy,pt[1])
    graph = [['.' for _ in range(maxx+1)] for _ in range(maxy+1) ]
    for pt in pts:
        if pt[0] > maxx or pt[1] > maxy:
            print(pt)
            continue
        graph[pt[1]][pt[0]] = '#'
    for line in graph:
        print(line)
    
draw(pts)