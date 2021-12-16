fname = input()
f = open(fname+".txt")
line = f.readline()
packet = ''
for x in line:
    no = int(x,16)
    bi = bin(no)[2:].zfill(4)
    packet += str(bi)
# converts packet to number

def compute(val,type):
    if type == 0:
        return sum(val)
    elif type == 1:
        res = 1
        for x in val:
            res*=x
        return res
    elif type == 2:
        return min(val)
    elif type == 3:
        return max(val)
    elif type == 5:
        return val[0] > val[1]
    elif type == 6:
        return val[0] < val[1]
    elif type == 7:
        return val[0] == val[1]

def convert(str):
    version = int(str[0:3],2)
    type = int(str[3:6],2)
    str = str[6:]
    if type == 4:
        res = ''
        i = 0
        last = False
        while last == False:
            for j in range(5):
                indx = i*5+j
                if j == 0:
                    if str[indx] == '0':
                        last = True
                    continue
                res += str[indx]
            i+=1
        return int(res,2),i*5+6
    else:
       type2 = str[0]
       st = 1
       if type2 == '0':
           en = st + 15
           totalLen = int(str[st:en],2)
           nowlen = 0
           str = str[en:]
           val = []

           while nowlen < totalLen:
               nowpacket,len2 = convert(str)
               str = str[len2:]
               val.append(nowpacket)
               nowlen += len2
           return compute(val,type),nowlen+22
       else: 
           en = st + 11
           nop = int(str[st:en],2)
           tempp = 0
           str = str[en:]
           tlen = 0
           val = []
           while tempp < nop:
               nowpacket,len2 = convert(str)
               tlen += len2
               str = str[len2:]
               val.append(nowpacket)
               tempp +=1
           return compute(val,type),tlen+18
res,_ = convert(packet)
print(res)
