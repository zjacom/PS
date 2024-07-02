from collections import deque
import sys

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[sys.maxsize] * m for _ in range(n)]

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

for y in range(n):
    for x in range(m):
        if graph[y][x] == 2:
            sy, sx = y, x
            break

q = deque([(sy, sx)])
visited[sy][sx] = 0

while q:
    y, x = q.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if visited[ny][nx] == sys.maxsize and graph[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))

for y in range(n):
    for x in range(m):
        if visited[y][x] == sys.maxsize:
            if graph[y][x]:
                visited[y][x] = -1
            else:
                visited[y][x] = 0

for row in visited:
    print(*row)