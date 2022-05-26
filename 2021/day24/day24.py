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
        if len(temp) > 0:
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

# This is a special program, the below code only works for the input ALU not for a generalized ALU
# For generalized ALU it will take 9^14 computations 

# Each block, C's are constants
# Initial State = (x,y,z) | (0,0,0)
# input w (0-9)
# x = z % 26
# if z_truncate:
#   z = z // 26
# if (z % 26) + C0 != input:
#   z = z * 26 + C3 + input
#   y = input + C3
# else:
#   x = 0
#   y = 0

# C0 - line 4 always greater than 10 whenever z_truncate is false !!!!!
# C1 - line 8 (always 25)
# C2 - line 10 (always 1)
# C3 - line 14

class Chunk:
    def __init__(self, z_truncate, x_incr, y_incr) -> None:
        self.z_truncate = z_truncate
        self.x_incr = x_incr
        self.y_incr = y_incr
    def printChunk(self):
        print("[Truncate]:",self.z_truncate,"[x_incr]:",self.x_incr,"[y_incr]:",self.y_incr)
chunks = []
for com in comm:
    z_truncate = False
    if com[3][3] == 26:
        z_truncate = True
    chunks.append(Chunk(z_truncate,com[4][3],com[14][3]))

# If Truncate is False, TempVariable =  input + y_incr
# Else input = x_incr + lastUsedTempVariable

program = []
variableStack = []
variableNo = -1
for idx,chunk in enumerate(chunks):
    if chunk.z_truncate == False:
        variableNo += 1
        varName = chr(ord('A')+variableNo)
        inpName = 'i' + str(idx)
        variableStack.append(varName)
        op = ' + '
        if chunk.y_incr < 0:
            op = ' ' 
        line = [varName,' = ',inpName,op,chunk.y_incr]
        program.append(line)
    else:
        varName = variableStack.pop()
        inpName = 'i' + str(idx)
        op = ' + '
        if chunk.x_incr < 0:
            op = ' '
        line = [inpName,' = ',varName,op,chunk.x_incr]     
        program.append(line)

for line in program:
    for c in line:
        print(c,end='')
    print("")

## final optimized ALU
# i3 = i2+5
# i5 = i4-3
# i7 = i6+7
# i10 = i9-1
# i11 = i8+3
# i12 = i1+6
# i13 = i0
# independent i0,i1,i2,i4,i6,i8,i9
# by hand Answer
# index 0| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13
# Max   9| 3 | 4 | 9 | 9 | 6 | 2 | 9 | 6 | 9 | 8  | 9  | 9  | 9 
# Min   1| 1 | 1 | 6 | 4 | 1 | 1 | 8 | 1 | 2 | 1  | 4  | 7  | 1