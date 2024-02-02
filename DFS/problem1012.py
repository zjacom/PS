import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY = [-1, 1, 0, 0]
dirX = [0, 0, 1, -1]


def dfs(y, x):
    global graph
    graph[y][x] = False

    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if graph[newY][newX]:
            dfs(newY, newX)


MAX = 50 + 10
result = []

T = int(input())

while T > 0:
    T -= 1
    M, N, K = map(int, input().split())
    graph = [[False] * MAX for _ in range(MAX)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y + 1][x + 1] = True

    count = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if graph[i][j]:
                dfs(i, j)
                count += 1

    result.append(count)

for cnt in result:
    print(cnt)