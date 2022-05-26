import itertools
fname = input()
f = open(fname+".txt")
last = -1
res = 0
nos = []
for x in f:
    nos.append(int(x))
n = len(nos)
psum = list(itertools.accumulate(nos))
for i in range(2,n):
    no = psum[i]
    if i > 2:
        no-= psum[i-3]
    if last > 0 and no > last:
        res+=1
    last = no
print(res)
f.close()