
def stringToDigit(str,):
    map = {}
    map["abcefg"] = 0
    map["cf"] = 1
    map["acdeg"] = 2
    map["acdfg"] = 3
    map["bcdf"] = 4
    map["abdfg"] = 5
    map["abdefg"] = 6
    map["acf"] = 7
    map["abcdefg"] = 8
    map["abcdfg"] = 9
    return map[str]

def transform(l0,l1):
    # map a-g from l0 to a-g in real
    freq = [0]*7
    str = "abcdefg"
    for i in range(7):
        for s in l0:
            for c in s:
                if c == str[i]:
                    freq[i]+=1
    revmap = {}
    for i in range(7):
        if freq[i] == 4:
            revmap[str[i]] = 'e'
        if freq[i] == 9:
            revmap[str[i]] = 'f'
        if freq[i] == 6:
            revmap[str[i]] = 'b'
    
    for s in l0:
        n = len(s)
        if n == 2:
            for c in s:
                if revmap.__contains__(c) == False:
                    revmap[c] = 'c'
    for s in l0:
        n = len(s)
        if n == 3:
            for c in s:
                if revmap.__contains__(c) == False:
                    revmap[c] = 'a'
    for s in l0:
        n = len(s)
        if n == 4:
            for c in s:
                if revmap.__contains__(c) == False:
                    revmap[c] = 'd'
    for s in l0:
        n = len(s)
        if n == 7:
            for c in s: 
                if revmap.__contains__(c) == False:
                    revmap[c] = 'g'
    no = 0
    for s in l1:
        newstr = ''
        for c in s:
            newstr += revmap[c]
        newstr = ''.join(sorted(newstr))
        no *=10
        no += stringToDigit(newstr)
    return no    

fname = input()
f = open(fname+".txt")


# a - 8
# b - 6
# c - 8
# d - 7
# e - 4
# f - 9
# g - 7

# 1 - 2
# 4 - 4
# 7 - 3
# 8 - 7
res = 0
for line in f:
    l = line.split('|')
    l0 = list(l[0][0:-1].split(' '))
    l1 = list(l[1][1:-1].split(' '))
    res += transform(l0,l1)
        
print(res)
