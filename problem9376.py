from collections import deque
import sys

TC = int(input())
result = []
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(cy, cx):
    visited = [[-1] * (w + 2) for _ in range(h + 2)]
    visited[cy][cx] = 0

    q = deque([(cy, cx)])
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < h + 2 and 0 <= nx < w + 2:
                if visited[ny][nx] == -1:
                    if graph[ny][nx] == "#":
                        visited[ny][nx] = visited[y][x] + 1
                        q.append((ny, nx))
                    elif graph[ny][nx] == "." or graph[ny][nx] == "$":
                        visited[ny][nx] = visited[y][x]
                        q.appendleft((ny, nx))
    return visited


for _ in range(TC):
    h, w = map(int, input().split())
    graph = [["."] * (w + 2)]
    for _ in range(h):
        graph.append(["."] + list(input().strip()) + ["."])
    graph.append(["."] * (w + 2))

    points = []
    for y in range(h + 2):
        for x in range(w + 2):
            if graph[y][x] == "$":
                points.append((y, x))
    
    c1 = bfs(points[0][0], points[0][1])
    c2 = bfs(points[1][0], points[1][1])
    sang = bfs(0, 0)

    answer = sys.maxsize

    for y in range(1, h + 1):
        for x in range(1, w + 1):
            if c1[y][x] != -1 and c2[y][x] != -1 and sang[y][x] != -1:
                cnt = c1[y][x] + c2[y][x] + sang[y][x]
                if graph[y][x] == "#":
                    answer = min(answer, cnt - 2)
                else:
                    answer = min(answer, cnt)

    result.append(answer)

for res in result:
    print(res)