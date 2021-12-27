fname = input()
f = open(fname+".txt")
p1 = int(f.readline().split("\n")[0].split(" ")[-1])
p2 = int(f.readline().split("\n")[0].split(" ")[-1])

dp = {}
dp[tuple([p1,p2,0,0])] = 1
q = []
q.append([p1,p2,0,0,0]) # p1 , p2 , s1 , s2 , turn
sum1 = 0
sum2 = 0
# while len(q) > 0:
#     top = q.pop(-1)
#     # print(sum1,sum2)
#     no = dp[tuple([top[0],top[1],top[2],top[3]])]
#     if top[2] >= 21:
#         sum1 += no
#         continue
#     elif top[3] >= 21:
#         sum2 += no
#         continue
#     for i in range(1,4):
#         for j in range(1,4):
#             for k in range(1,4):
#                 turn = 1 - top[4]
#                 if top[4] == 0:
#                     nxt = (i + j + k + top[0])%10
#                     if nxt == 0:
#                         nxt = 10
#                     q.append([nxt,top[1],top[2]+nxt,top[3],turn])
#                     tup = tuple([nxt,top[1],top[2]+nxt,top[3]])
#                     if dp.__contains__(tup):
#                         dp[tup] += no
#                     else:
#                         dp[tup] = no
#                 else:
#                     nxt = (i + j + k + top[1])%10
#                     if nxt == 0:
#                         nxt = 10
#                     q.append([top[0],nxt,top[2],top[3]+nxt,turn])
#                     tup = tuple([top[0],nxt,top[2],top[3]+nxt])
#                     if dp.__contains__(tup):
#                         dp[tup] += no
#                     else:
#                         dp[tup] = no

def recurse(tup):
    ...
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                if tup[4] == 0:
                    ...
                    
                else:
                    ...


recurse((p1,p2,0,0,0))
print(max(sum1,sum2))
