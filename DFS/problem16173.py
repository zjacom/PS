import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
MAX = 3 + 100 + 10
graph = [[0] * MAX for _ in range(MAX)]
result = "Hing"


def dfs(y, x):
    global graph, result
    print(y, x)

    if graph[y][x] == -1:
        result = "HaruHaru"
        return

    cur = graph[y][x]
    graph[y][x] = 0

    dirY = [0, cur]
    dirX = [cur, 0]

    for i in range(2):
        if graph[y + dirY[i]][x + dirX[i]] != 0:
            dfs(y + dirY[i], x + dirX[i])


for i in range(N):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        graph[i][j] = row[j]

dfs(0, 0)
print(result)