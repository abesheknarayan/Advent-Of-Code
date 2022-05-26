fname = input()
f = open(fname+".txt")
fish = list(map(int,f.readline().split(',')))
freq = [0]*9
for fi in fish:
    freq[fi]+=1
for i in range(256):
    newfreq = [0]*9
    for j in range(9):
        if j == 0:
            newfreq[6] += freq[j]
            newfreq[8] += freq[j]
        else :
            newfreq[j-1] += freq[j]
    freq = newfreq
print(sum(freq))