fname = input()
f = open(fname+".txt")
line = f.readline()
packet = ''
for x in line:
    no = int(x,16)
    bi = bin(no)[2:].zfill(4)
    packet += str(bi)
# converts packet to number
def convert(str):
    version = int(str[0:3],2)
    type = str[3:6]
    str = str[6:]
    if type == '100':
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
        return version,i*5+6
    else:
       type2 = str[0]
       st = 1
       if type2 == '0':
           en = st + 15
           totalLen = int(str[st:en],2)
           nowlen = 0
           str = str[en:]
           val = version
           while nowlen < totalLen:
               nowpacket,len2 = convert(str)
               str = str[len2:]
               val += nowpacket
               nowlen += len2
           return val,nowlen+22
       else: 
           en = st + 11
           nop = int(str[st:en],2)
           tempp = 0
           str = str[en:]
           tlen = 0
           val = version
           while tempp < nop:
               nowpacket,len2 = convert(str)
               tlen += len2
               str = str[len2:]
               val += nowpacket
               tempp +=1
           return val,tlen+18
res,_ = convert(packet)
print(res)
