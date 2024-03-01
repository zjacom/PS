N = int(input())

graph = []

for _ in range(N):
    graph.append(list(input().strip()))

answer = 0
dirY, dirX = [-1, -1, 0, 0, 1, 1], [0, 1, -1, 1, -1, 0]
visited = [[0] * N for _ in range(N)]

def dfs(y, x):
    global answer
    answer = max(answer, 1)

    for i in range(6):
        ny, nx = y + dirY[i], x + dirX[i]
        if 0 <= ny < N and 0 <= nx < N:
            if graph[ny][nx] == "X":
                if not visited[ny][nx]:
                    visited[ny][nx] = -visited[y][x]
                    dfs(ny, nx)
                    answer = max(answer, 2)
                else:
                    if visited[ny][nx] == visited[y][x]:
                        answer = max(answer, 3)
                        return

for y in range(N):
    for x in range(N):
        if graph[y][x] == "X":
            if not visited[y][x]:
                visited[y][x] = 1
                dfs(y, x)

print(answer)