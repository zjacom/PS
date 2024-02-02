import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
MAX = 50 + 10
graph = [["d"] * MAX for _ in range(MAX)]

for h in range(N):
    row = input()
    for tile in range(M):
        graph[h][tile] = row[tile]


def hypen_dfs(y, x):
    if graph[y][x] == "-":
        graph[y][x] = "d"

        hypen_dfs(y, x + 1)


def vertical_dfs(y, x):
    if graph[y][x] == "|":
        graph[y][x] = "d"

        vertical_dfs(y + 1, x)


result = 0
for y in range(N):
    for x in range(M):
        if graph[y][x] == "-":
            hypen_dfs(y, x)
            result += 1
        elif graph[y][x] == "|":
            vertical_dfs(y, x)
            result += 1
print(result)