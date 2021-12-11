fname = input()
f = open(fname+".txt")
res = 0
for line in f:
    line = list(line.split('\n')[0])
    st = []
    finc = ''
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
    if finc == ')':
        res += 3
    elif finc == '}':
        res += 1197
    elif finc == ']':
        res += 57
    elif finc == '>':
        res+= 25137
print(res)