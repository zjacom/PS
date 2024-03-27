# 6087번

from collections import deque
import sys

W, H = map(int, input().split())

graph = [list(map(str, input().strip())) for _ in range(H)]
points = []
for y in range(H):
    for x in range(W):
        if graph[y][x] == "C":
            points.append((y, x))
            graph[y][x] = "."

sy, sx, ey, ex = points[0][0], points[0][1], points[1][0], points[1][1]

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

q = deque()

visited = [[[sys.maxsize] * 4 for _ in range(W)] for _ in range(H)]

for i in range(4):
    ny, nx = sy + dy[i], sx + dx[i]
    if 0 <= ny < H and 0 <= nx < W:
        if graph[ny][nx] == ".":
            q.append((ny, nx, i))
            visited[ny][nx][i] = 0

while q:
    y, x, prev = q.popleft()

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < H and 0 <= nx < W:
            if graph[ny][nx] == ".":
                cnt = visited[y][x][prev]
                if prev == 0 or prev == 1:
                    if i == 2 or i == 3:
                        cnt += 1
                else:
                    if i == 0 or i == 1:
                        cnt += 1
                
                if visited[ny][nx][i] > cnt:
                    visited[ny][nx][i] = cnt
                    q.append((ny, nx, i))

print(min(visited[ey][ex]))