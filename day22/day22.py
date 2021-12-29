fname = input()
f = open(fname+".txt")
coms = []

def do(line):
    return sorted(tuple(map(int,line.split("=")[1].split(".."))))
    
for line in f:
    line = line.split("\n")[0]
    line = line.split(" ")
    cords = line[1].split(",")
    coms.append([line[0],tuple([tuple(do(cords[0])),tuple(do(cords[1])),tuple(do(cords[2]))])])


def valid(com):
    for i in range(3):
        for j in range(2):
            if com[i][j] > 50 or com[i][j] < -50:
                return False
    return True

pts = set()
for com in coms:
    if valid(com[1]) == False:
        continue
    for i in range(com[1][0][0],com[1][0][1]+1):
        for j in range(com[1][1][0],com[1][1][1]+1):
            for k in range(com[1][2][0],com[1][2][1]+1):
                if com[0] == 'on':
                    pts.add((i,j,k))
                else:
                    ...
                    if pts.__contains__((i,j,k)):
                        pts.remove((i,j,k))

print(len(pts))

# for part 2 , there should be some cube region add / deletion algo
# first lets consider adding cuboids
# Lets maintain all the active cuboids as non intersecting (edges can intersect but not the volume)
# when a cuboid is added, 
#  1. we need to find if its already covered by any other cuboid?
#  2. else if its just intersecting, split the cuboids into multiple smaller cuboids removing the intersected regions 
#  3. step 2 is the harder part
# some recursion stuff to be done for each intersecting areas



# returns the intersection cube of given 2 cubes
def findIntersectionCube(cube1,cube2):
    cube = []
    for i in range(3):
        if cube1[i][0] > cube2[i][1] or cube2[i][0] > cube1[i][1]:
            return -1
        if max(cube1[i]) >= max(cube2[i]) and min(cube1[i]) <= min(cube2[i]):
            cube.append(cube2[i])
            continue
        if max(cube2[i]) >= max(cube1[i]) and min(cube2[i]) <= min(cube1[i]):
            cube.append(cube1[i])
            continue
        if cube1[i][1] > cube2[i][1]:
            cube.append(tuple(sorted((cube1[i][0],cube2[i][1]))))
        else:
            cube.append(tuple(sorted((cube2[i][0],cube1[i][1]))))
    return tuple(cube)


# returns the volume of cube
def getVolumeOfCube(cube):
    volume = 1
    for i in range(3):
        volume*=(cube[i][1]-cube[i][0]+1)
    return volume

import collections

# returns the total volume occupied by the list of cubes
def getVolumeOfCubeList(cubes):
    cubeMap = collections.Counter()
    for cube in cubes:
        newCubeMap = collections.Counter()
        for vcube,val in cubeMap.items(): 
            intersection = findIntersectionCube(cube[1],vcube)
            if intersection != -1:
                newCubeMap[intersection] -= val
        if cube[0] == 'on':
            newCubeMap[cube[1]] += 1
        cubeMap.update(newCubeMap)
    result = 0
    for cube,val in cubeMap.items():
        result += val*getVolumeOfCube(cube)
    return result
cubeList = []
for com in coms:
    cubeList.append(com)
print(getVolumeOfCubeList(cubeList))