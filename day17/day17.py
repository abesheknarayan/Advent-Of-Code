fname = input()
f = open(fname+".txt")
n = 400
grid = [['.' for _ in range(n)] for _ in range(n)]

inp = f.readline()
inp = inp.split("\n")[0].split("target area: ")[1]
inp = inp.split(" ")
xx = list(map(int,inp[0].split("x=")[1].split("..")))
yy = list(map(int,inp[1].split("y=")[1].split("..")))
xx.sort()
yy.sort()

def inside(xp,yp,xx,yy):
    return xp >= xx[0] and xp <= xx[1] and yp >= yy[0] and yp <= yy[1]

def changeVelocity(vx,vy):
    if vx > 0:
        vx-=1
    elif vx < 0:
        vx +=1
    vy-=1
    return vx,vy

# returns if its collides and max y 
def project(xx,yy,vx,vy):
    px = 0
    py = 0
    maxy = -1000
    for _ in range(300):
        px += vx
        py += vy
        maxy = max(maxy,py)
        vx,vy = changeVelocity(vx,vy)     
        if inside(px,py,xx,yy):
            return True,maxy
    return False,-1

maxy = -1000
count = 0
for vx in range(-300,301):
    for vy in range(-300,301):
            ok,y = project(xx,yy,vx,vy)
            if ok :
                count += 1
                maxy = max(maxy,y)
print(count)
print(maxy)


