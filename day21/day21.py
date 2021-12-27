fname = input()
f = open(fname+".txt")
p1 = int(f.readline().split("\n")[0].split(" ")[-1])
p2 = int(f.readline().split("\n")[0].split(" ")[-1])

s1 = 0
s2 = 0
turn = False
number = 1
turns = 0
while True:
    if s1 >= 1000 or s2 >= 1000:
        print(min(s1,s2)*(turns)*3)
        break
    if turn == False:
        p1 += 3*(number+1)
        p1%=10
        if p1 == 0:
            p1 = 10
        s1 += p1
    else:
        p2 += 3*(number+1)
        p2%=10
        if p2 == 0:
            p2 = 10
        s2 += p2
    turn = not turn
    number += 3
    turns+=1

