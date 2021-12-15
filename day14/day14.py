fname = input()
f = open(fname+".txt")
poly = str(f.readline().split("\n")[0])
f.readline()
rules = []
for line in f:
    line = line.split("\n")[0]
    line = line.split(" -> ")
    rules.append(line)
n = len(poly)
polyg = [[0 for _ in range(26)] for _ in range(26)]
cref = ord('A')
fi = ord(poly[0])-cref
en = ord(poly[n-1])-cref
for i in range(n-1):
    polyg[ord(poly[i])-cref][ord(poly[i+1])-cref]+=1

for step in range(40):
    newpoly = [[0 for _ in range(26)] for _ in range(26)]
    for i in range(26):
        for j in range(26):
            if polyg[i][j] == 0:
                continue
            str = chr(cref+i) + chr(cref+j)
            for rule in rules:
                if rule[0] == str:
                    newpoly[i][ord(rule[1])-cref]+=polyg[i][j]
                    newpoly[ord(rule[1])-cref][j]+=polyg[i][j]
    polyg = newpoly

freq = [0 for _ in range(26)]
for i in range(26):
    for j in range(26):
        freq[i]+=polyg[i][j]
        freq[j]+=polyg[i][j]
freq[fi]+=1
freq[en]+=1
mini = 10**14
for i in range(26):
    if freq[i] > 0:
        mini = min(mini,freq[i])
print(max(freq)//2 - mini//2)
