def mark(no,boards,visited,noOfBoards):
    for i in range(noOfBoards):
        for j in range(5):
            for k in range(5):
                if boards[i][j][k] == no:
                    visited[i][j][k] = 1

def checkRow(arr):
    for i in range(5):
        filled = 0
        for j in range(5):
            if arr[i][j] == 1:
                filled+=1
        if filled == 5:
            return True
    return False

def checkCol(arr):
    for i in range(5):
        filled = 0
        for j in range(5):
            if arr[j][i] == 1:
                filled+=1
        if filled == 5:
            return True
    return False

def check(visited,noOfBoards):
    # check if any row or any column is completely filled
    for i in range(noOfBoards):
        ok = checkRow(visited[i]) or checkCol(visited[i])
        if ok :
            return i
    return -1

def compute(arr,visited):
    sum = 0
    for i in range(5):
        for j in range(5):
            if visited[i][j] == 0:
                sum += arr[i][j]
    return sum


fname = input()
f = open(fname+".txt")
randomNos = list(map(int,f.readline().split('\n')[0].split(',')))
noOfBoards = 0
board = []
boards = []
f.readline()
for line in f:
    if line == '\n':
        boards.append(board)
        board = []
        continue
    noOfBoards+=1
    nowRow = list(line.split('\n')[0].split(' '))
    sanitizedRow = []
    for x in nowRow:
        if x == '':
            continue
        sanitizedRow.append(int(x))
    board.append(sanitizedRow)
boards.append(board)
noOfBoards //= 5
# correct way of doing multi dimensional independent ref lists
visited = [[[0 for _ in range(5)]for _ in range(5)]for _ in range(noOfBoards)]
winner = -1
last = -1
for no in randomNos:
    mark(no,boards,visited,noOfBoards)
    winner = check(visited,noOfBoards)
    last = no
    if winner != -1:
        break

print(compute(boards[winner],visited[winner])*last)