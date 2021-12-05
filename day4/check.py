def changeSomething(arr):
    arr[0] = 4

# arr2 = [1,2,3,4]
# print(arr2)
# changeSomething(arr2)
# print(arr2)
visited = [[0 for i in range(5)]for _ in range(5)]
print(visited)
visited[0][0] = 1
print(visited)