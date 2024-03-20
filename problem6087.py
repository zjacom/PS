from collections import deque
import sys

W, H = map(int, input().split())

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
graph = []
point = []
visited = [[[sys.maxsize] * 4 for _ in range(W)] for _ in range(H)]

for idx in range(H):
    temp = []
    value = list(input().strip())
    for jdx, v in enumerate(value):
        if v == "C":
            point.append((idx, jdx))
            temp.append(("."))
        else:
            temp.append(v)
    graph.append(temp)

q = deque()

start_y, start_x = point[0][0], point[0][1]

for i in range(4):
    ny, nx = start_y + dy[i], start_x + dx[i]
    if 0 <= ny < H and 0 <= nx < W:
        if graph[ny][nx] != "*":
            q.append((ny, nx, i))
            visited[ny][nx][i] = 0

answer = sys.maxsize

while q:
    y, x, way = q.popleft()

    if y == point[1][0] and x == point[1][1]:
        answer = min(answer, visited[y][x][way])
    
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < H and 0 <= nx < W:
            if graph[ny][nx] != "*":
                cnt = visited[y][x][way]
                if way == 0 or way == 1:
                    if i == 2 or i == 3:
                        cnt += 1
                else:
                    if i == 1 or i == 0:
                        cnt += 1
                if cnt < visited[ny][nx][i]:
                    visited[ny][nx][i] = cnt
                    q.append((ny, nx, i))

print(answer)