# 6087번
from collections import deque
import sys

W, H = map(int, input().split())

graph = [list(input().strip()) for _ in range(H)]
points = []
visited = [[[sys.maxsize] * 4 for _ in range(W)] for _ in range(H)]
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

for y in range(H):
    for x in range(W):
        if graph[y][x] == "C":
            points.append((y, x))

q = deque()
for i in range(4):
    ny, nx = points[0][0] + dy[i], points[0][1] + dx[i]
    if 0 <= ny < H and  0 <= nx < W:
        if graph[ny][nx] != "*":
            visited[ny][nx][i] = 0
            q.append((ny, nx, i))

while q:
    y, x, d = q.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < H and  0 <= nx < W:
            if graph[ny][nx] != "*":
                if i == 0 or i == 1:
                    if d == 2 or d == 3:
                        if visited[y][x][d] + 1 < visited[ny][nx][i]:
                            q.append((ny, nx, i))
                            visited[ny][nx][i] = visited[y][x][d] + 1
                    else:
                        if visited[y][x][d] < visited[ny][nx][i]:
                            q.append((ny, nx, i))
                            visited[ny][nx][i] = visited[y][x][d]
                if i == 2 or i == 3:
                    if d == 0 or d == 1:
                        if visited[y][x][d] + 1 < visited[ny][nx][i]:
                            q.append((ny, nx, i))
                            visited[ny][nx][i] = visited[y][x][d] + 1
                    else:
                        if visited[y][x][d] < visited[ny][nx][i]:
                            q.append((ny, nx, i))
                            visited[ny][nx][i] = visited[y][x][d]

print(min(visited[points[1][0]][points[1][1]]))