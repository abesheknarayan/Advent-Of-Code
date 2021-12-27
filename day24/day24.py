fname = input()
f = open(fname+".txt")
comm = []
temp = []

def resolveVariableName(name):
    if len(name) != 1:
        return -1
    return ord(name) - ord('w')

for line in f:
    line = line.split("\n")[0]
    if line.__contains__("inp w"):
        comm.append(temp)
        temp = []
    else:
        line = line.split(" ")
        if resolveVariableName(line[2]) in range(0,4):
            temp.append([line[0],1,resolveVariableName(line[1]),resolveVariableName(line[2])])  
        else:    
            temp.append([line[0],2,resolveVariableName(line[1]),int(line[2])])
if len(temp) > 0:
    comm.append(temp)


def loadValue(x,vals):
    return vals[x]
def setValue(x,vals,val):
    vals[x] = val
    return vals

def getTupleZ(val):
    return tuple([val//26,val%26])
    
def getAdd(c1,c2,c3,vals):
    a = loadValue(c2,vals)
    if c1 == 1:
        b = loadValue(c3,vals)
    else:
        b = c3
    if c2 == 3 and c1 == 1:
        a = getTupleZ((a[0]*26+a[1])+b)
    elif c3 == 3 and c1 == 1:
        a = a + b[1]
    else:
        a = a + b
    vals = setValue(c2,vals,a)
    return vals

def getMul(c1,c2,c3,vals):
    a = loadValue(c2,vals)
    if c1 == 1:
        b = loadValue(c3,vals)
    else:
        b = c3
    if c2 == 3:
        a = getTupleZ((a[0]*26+a[1])*b)
    else:
        a = a * b
    vals = setValue(c2,vals,a)
    return vals

def getDiv(c1,c2,c3,vals):
    a = loadValue(c2,vals)
    if c1 == 1:
        b = loadValue(c3,vals)
    else:
        b = c3
    if c2 == 3:
        if b == 1:
            ...
        elif b == 26:
            ...
            a = getTupleZ(a[0])
    else:        
        a = a // b
    vals = setValue(c2,vals,a)
    return vals

def getMod(c1,c2,c3,vals):
    a = loadValue(c2,vals)
    if c1 == 1:
        b = loadValue(c3,vals)
    else:
        b = c3
    a = a % b
    vals = setValue(c2,vals,a)
    return vals

def getEql(c1,c2,c3,vals):
    a = loadValue(c2,vals)
    if c1 == 1:
        b = loadValue(c3,vals)
    else:
        b = c3
    if a == b:
        a = 1
    else:
        a = 0
    vals = setValue(c2,vals,a)
    return vals

# find the largest digit we can get from the list of sequential commands
def findLargestDigit(com,prevState):
    res = set()
    tupleMap = {}
    for state in prevState:
        prevRes = state[0]
        for i in range(1,10):
            vals = list(state[1])
            vals[0] = i
            for c in com:
                if c[0] == 'add':
                    vals = getAdd(c[1],c[2],c[3],vals)
                elif c[0] == 'mul':
                    vals = getMul(c[1],c[2],c[3],vals)    
                elif c[0] == 'div':
                    vals = getDiv(c[1],c[2],c[3],vals)     
                elif c[0] == 'mod':
                    vals = getMod(c[1],c[2],c[3],vals)     
                elif c[0] == 'eql':
                    vals = getEql(c[1],c[2],c[3],vals)
            nowRes = prevRes*10 + i
            valss = tuple(vals)
            if tupleMap.__contains__(valss) == False:
                tupleMap[valss] = nowRes
            else:
                tupleMap[valss] = max(tupleMap[valss],nowRes)

    for t in tupleMap:
        res.add(tuple([tupleMap[t],t]))
    return res

comm.pop(0)
prevState = set()
prevState.add(tuple([0,tuple([0,0,0,tuple([0,0])])]))
for com in comm:
    print(len(prevState))
    prevState = findLargestDigit(com,prevState)

res = 0
for state in prevState:
    if state[1][3] == tuple([0,0]):       
        res = max(res,state[0])
print(res)