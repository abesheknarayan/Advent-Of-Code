fname = input()
f = open(fname+".txt")
res = []
for line in f:
    line = list(line.split('\n')[0])
    st = []
    finc = '-'
    for c in line :
        if c == '(' or c == '{' or c == '[' or c == '<':
            st.append(c)
        else:
            if len(st) == 0:
                finc = c
                break
            else:
                cc = st[len(st)-1]
                if cc == '(' and c == ')':
                    st.pop()
                elif cc == '[' and c == ']':
                    st.pop()
                elif cc == '{' and c == '}':
                    st.pop()
                elif cc == '<' and c == '>':
                    st.pop()
                else:
                    finc = c
                    break
    if finc != '-':
        continue
    tans = 0
    
    for i in range(len(st)-1,-1,-1):
        tans*=5
        c = st[i]
        if c == '(':
            tans += 1
        elif c == '[':
            tans+=2
        elif c == '{':
            tans+=3
        elif c== '<':
            tans+=4
    res.append(tans)
res.sort()
n = len(res)
print(res[n//2])