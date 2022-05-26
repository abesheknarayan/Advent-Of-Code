import itertools
fname = input()
f = open(fname+".txt")
freq = [0]*20
n = 0
for line in f: 
    n = len(line)
    for indx,bit in enumerate(line):
        if bit == '\n': 
            continue
        no = int(bit)
        if no == 0:
            freq[indx]-=1
        else:
            freq[indx]+=1

gamma = 0
epsilon = 0
p2 = 1
for i in range(n-1,-1,-1):
    if freq[i] >= 0:
        gamma += p2
    else :
        epsilon += p2
    p2*=2

print(gamma,epsilon,gamma*epsilon)