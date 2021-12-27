fname = input()
f = open(fname+".txt")
coms = []

def do(line):
    return list(map(int,line.split("=")[1].split("..")))
    
for line in f:
    line = line.split("\n")[0]
    line = line.split(" ")
    cords = line[1].split(",")
    coms.append([line[0],do(cords[0]),do(cords[1]),do(cords[2])])


def valid(com):
    for i in range(3):
        for j in range(2):
            if com[i+1][j] > 50 or com[i+1][j] < -50:
                return False
    return True

pts = set()
for com in coms:
    if valid(com) == False:
        continue
    for i in range(com[1][0],com[1][1]+1):
        for j in range(com[2][0],com[2][1]+1):
            for k in range(com[3][0],com[3][1]+1):
                if com[0] == 'on':
                    pts.add((i,j,k))
                else:
                    if pts.__contains__((i,j,k)):
                        pts.remove((i,j,k))

print(len(pts))

