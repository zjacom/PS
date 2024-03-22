import sys
from collections import deque

answer = []
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
T = int(input())

def bfs(y, x):
    visited = [[0] * (w + 2) for _ in range(h + 2)]

    q = deque([(y, x, 0)])

    while q:
        cy, cx, cnt = q.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < h + 2 and 0 <= nx < w + 2:
                if not visited[ny][nx] and graph[ny][nx] != '*':
                    visited[ny][nx] = 1
                    if dist[ny][nx] < 0:
                        dist[ny][nx] = 0
                    if graph[ny][nx] == "#":
                        q.append((ny, nx, cnt + 1))
                        dist[ny][nx] += cnt + 1
                    else:
                        q.appendleft((ny, nx, cnt))
                        dist[ny][nx] += cnt


for _ in range(T):
    h, w = map(int, input().split())
    graph = [['.'] * (w + 1)]
    for _ in range(h):
        graph.append(['.'] + list(input()) + ['.'])
    graph.append(['.'] * (w + 1))

    dist = [[-1] * (w + 2) for _ in range(h + 2)]

    prisoners = []
    for i in range(h):
        for j in range(w):
            if graph[i+1][j+1] == "$":
                prisoners.append((i+1, j+1))
                graph[i+1][j+1] = '.'

    bfs(prisoners[0][0], prisoners[0][1])
    bfs(prisoners[1][0], prisoners[1][1])
    bfs(0, 0)

    answer = sys.maxsize
    for y in range(1, h + 1):
        for x in range(1, w + 1):
            if dist[y][x] == -1:
                continue
            if graph[y][x] == "#":
                answer = min(answer, dist[y][x] - 2)
            elif graph[y][x] == '.':
                answer = min(answer, graph[y][x])
    print(answer)