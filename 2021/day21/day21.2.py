fname = input()
f = open(fname+".txt")
p1 = int(f.readline().split("\n")[0].split(" ")[-1])
p2 = int(f.readline().split("\n")[0].split(" ")[-1])

# we have this tree kindof structure with each node having 3 children (universes)
# should do some recursion stuff
# assuming each player still rolls the dice 3 times

ways = {}
# (current_p1, current_p2, turn , score_p1 , score_p2): number of ways to that state

c = [x+y+z for x in [1,2,3] for y in [1,2,3] for z in [1,2,3]]

# given initial starting state as parameter, this function returns a list of 2 numbers --> the number of ways in which p1,p2 can win
def go(p1_x,p2_x,turn,p1_s = 0,p2_s = 0):
    tup = (p1_x,p2_x,turn,p1_s,p2_s)
    if tup in ways:
        return ways[tup]
    res = [0,0]
    for now in c:
        if turn == 0:
            newp1_x = (now + p1_x - 1) % 10 + 1
            newp1_s = p1_s + newp1_x
            if newp1_s >= 21:
                res[0] += 1
            else:
                tans = go(newp1_x,p2_x,1-turn,newp1_s,p2_s)
                res = [a+b for a,b in zip(res,tans)]
        else:
            newp2_x = (now + p2_x - 1) % 10 + 1
            newp2_s = p2_s + newp2_x
            if newp2_s >= 21:
                res[1] += 1
            else:
                tans = go(p1_x,newp2_x,1-turn,p1_s,newp2_s)
                res = [a+b for a,b in zip(res,tans)]
    ways[tup] = res
    return res
print(max(go(p1,p2,0)))