import itertools

def bstring_to_int(str):
    p2 = 1
    rstr = str[::-1]
    res = 0
    for x in rstr:
        no = int(x)
        res += no*p2
        p2*=2
    return res

def compute(arr,gindex,n):
    for i in range(0,n):
        if len(arr) == 1:
            break
        removed = []
        bit = 0
        for x in arr:
            no = int(x[i])
            if no == 0:
                bit-=1
            else:
                bit+=1
        
        if bit >= 0:
            bit = gindex
        else: 
            bit = 1 - gindex

        for x in arr:
            no = int(x[i])
            if no != bit:
                removed.append(x)
        for rem in removed:
            arr.remove(rem)
    return bstring_to_int(arr[0])

fname = input()
f = open(fname+".txt")
freq = [0]*20
n = 0
o2 = []
co2 = []
for line in f:
    n = len(line)
    bits = line.split('\n')[0]
    o2.append(bits)
    co2.append(bits)
print(compute(o2,1,n)*compute(co2,0,n))