from collections import deque
import sys
input = sys.stdin.readline
graph = []
dirY, dirX = [0, 0, -1, 1], [1, -1, 0, 0]

# 입력
N, M = map(int, input().split())
for _ in range(N):
    row = list(map(int, input().split()))
    graph.append(row)

# 로직
def func(y, x):
    global visited, graph
    visited[y][x] = True
    
    for i in range(4):
        newY, newX = y + dirY[i], x + dirX[i]
        if 0 <= newY <= N and 0 <= newX <= M and graph[newY][newX] == 0 and not visited[newY][newX]:
            graph[y][x] -= 1
    
    if graph[y][x] < 0:
        graph[y][x] = 0


def bfs(y, x):
    global graph, visited
    q = deque()
    q.append([y, x])

    while q:
        cy, cx = q.popleft()
        if visited[cy][cx]:
            continue
        visited[cy][cx] = True

        for i in range(4):
            ny, nx = cy + dirY[i], cx + dirX[i]
            if 0 <= ny <= N and 0 <= nx <= M:
                if not visited[ny][nx]:
                    if graph[ny][nx] != 0:
                        q.append([ny, nx])


# 출력
answer = 0
while True:
    answer += 1

    visited = [[False] * M for _ in range(N)]
    for y in range(1, len(graph) - 1):
        for x in range(len(graph[0])):
            if graph[y][x] != 0:
                func(y, x)

    if [[0] * M for _ in range(N)] == graph:
        answer = 0
        break
    
    count = 0
    visited = [[False] * M for _ in range(N)]
    for y in range(1, len(graph) - 1):
        for x in range(len(graph[0])):
            if graph[y][x] != 0 and not visited[y][x]:
                bfs(y, x)
                count += 1
    
    if count >= 2:
        break

print(answer)
