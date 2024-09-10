from collections import deque

r, c = map(int, input().split())

graph = [list(input()) for _ in range(r)]

fires = deque()
for y in range(r):
    for x in range(c):
        if graph[y][x] == "J":
            jy, jx = y, x
        if graph[y][x] == "F":
            fires.append((y, x))

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

def is_fire(y, x):
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < r and 0 <= nx < c:
            if graph[ny][nx] == "F":
                return True
    return False
    

def bfs():
    q = deque([(jy, jx)])
    visited = [[-1] * c for _ in range(r)]
    visited[jy][jx] = 0

    while q:
        for _ in range(len(q)):
            y, x = q.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if ny == -1 or ny == r or nx == -1 or nx == c:
                    return visited[y][x] + 1
                if not is_fire(ny, nx) and visited[ny][nx] == -1 and graph[ny][nx] == ".":
                    q.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
        
        for _ in range(len(fires)):
            y, x = fires.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < r and 0 <= nx < c:
                    if graph[ny][nx] == "." or graph[ny][nx] == "J":
                        graph[ny][nx] = "F"
                        fires.append((ny, nx))

result = bfs()
if result:
    print(result)
else:
    print("IMPOSSIBLE")