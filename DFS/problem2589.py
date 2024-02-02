from collections import deque
import sys
input = sys.stdin.readline

# input
column, row = map(int, input().split())
arr = []
for _ in range(column):
    arr.append(list(input().strip()))

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
result = 0

# logic
def bfs(y, x):
    global visited, arr, result
    q = deque([(y, x, 0)])
    visited[y][x] = True
    while q:
        cy, cx, cc = q.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < column and 0 <= nx < row:
                if not visited[ny][nx]:
                    if arr[ny][nx] == "L":
                        result = max(result, cc + 1)
                        visited[ny][nx] = True
                        q.append((ny, nx, cc + 1))

for y in range(column):
    for x in range(row):
        if arr[y][x] == "L":
            visited = [[False] * (row) for _ in range(column)]
            bfs(y, x)

# ouput
print(result)

