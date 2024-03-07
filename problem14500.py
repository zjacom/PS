import sys
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
dirY, dirX = [0, 0, 1, -1], [1, -1, 0, 0]
visited = [[False] * M for _ in range(N)]
maxi = -sys.maxsize

def recur(y, x, total, cnt):
    global maxi, visited
    visited[y][x] = True
    if cnt == 0:
        maxi = max(maxi, total)
        return
    for i in range(4):
        ny, nx = y + dirY[i], x + dirX[i]
        if 0 <= ny < N and 0 <= nx < M:
            if not visited[ny][nx]:
                recur(ny, nx, total + graph[y][x], cnt - 1)
                visited[ny][nx] = False

def func(y, x):
    global maxi
    for i in range(4):
        temp = graph[y][x]
        for j in range(3):
            ny, nx = y + dirY[(i + j) % 4], x + dirX[(i + j) % 4]
            if 0 <= ny < N and 0 <= nx < M:
                temp += graph[ny][nx]
            else:
                temp = 0
                break
        maxi = max(maxi, temp)

for y in range(N):
    for x in range(M):
        recur(y, x, 0, 4)
        visited[y][x] = False
        func(y, x)

print(maxi)