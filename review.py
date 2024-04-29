# 1600번
from collections import deque
import sys

k = int(input())
W, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]
visited = [[[sys.maxsize for _ in range(8)] for _ in range(W)] for _ in range(H)]
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
hy, hx = [-2, -2, -1, -1, 2, 2, 1, 1], [1, -1, 2, -2, 1, -1, 2, -2]
q = deque([(0, 0, k)])
for i in range(8):
    visited[0][0][i] = 0


def checker(y, x):
    return y < 0 or y >= H or x < 0 or x >= W


while q:
    y, x, K = q.popleft()

    if y == H - 1 and x == W - 1:
        if visited[y][x][K] == sys.maxsize:
            print(-1)
            exit(0)
        else:
            print(visited[y][x][K])
            exit(0)
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if checker(ny, nx):
            continue
        if graph[ny][nx] == 0:
            if visited[ny][nx][K] > visited[y][x][K] + 1:
                q.append((ny, nx, K))
                visited[ny][nx][K] = visited[y][x][K] + 1
    
    if K > 0:
        for i in range(8):
            ny, nx = y + hy[i], x + hx[i]
            if checker(ny, nx):
                continue
            if graph[ny][nx] == 0:
                if visited[ny][nx][K - 1] > visited[y][x][K] + 1:
                    q.append((ny, nx, K - 1))
                    visited[ny][nx][K - 1] = visited[y][x][K] + 1