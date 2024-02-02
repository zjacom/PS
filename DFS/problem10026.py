import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [["N"] * (N + 10) for _ in range(N + 10)]
dirY, dirX = [0, 0, 1, -1], [1, -1, 0, 0]

for y in range(1, N + 1):
    value = input()
    for x, v in enumerate(value):
        if v == "R":
            graph[y][x + 1] = v
        if v == "B":
            graph[y][x + 1] = v
        if v == "G":
            graph[y][x + 1] = v


def dfs(y, x, color):
    global graph, visited
    visited[y][x] = True

    for i in range(4):
        if graph[y + dirY[i]][x + dirX[i]] == color and not visited[y + dirY[i]][x + dirX[i]]:
            dfs(y + dirY[i], x + dirX[i], color)


visited = [[False] * (N + 10) for _ in range(N + 10)]
normal = 0
for y in range(1, N + 1):
    for x in range(1, N + 1):
        if graph[y][x] == "R"and not visited[y][x]:
            dfs(y, x, "R")
            normal += 1
        if graph[y][x] == "B"and not visited[y][x]:
            dfs(y, x, "B")
            normal += 1
        if graph[y][x] == "G"and not visited[y][x]:
            dfs(y, x, "G")
            normal += 1

for y in range(1, N + 1):
    for x in range(1, N + 1):
        if graph[y][x] == "G":
            graph[y][x] = "R"

visited = [[False] * (N + 10) for _ in range(N + 10)]
not_normal = 0
for y in range(1, N + 1):
    for x in range(1, N + 1):
        if graph[y][x] == "R"and not visited[y][x]:
            dfs(y, x, "R")
            not_normal += 1
        if graph[y][x] == "B"and not visited[y][x]:
            dfs(y, x, "B")
            not_normal += 1

print(normal, not_normal)