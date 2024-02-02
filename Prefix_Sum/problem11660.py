import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# logic
prefix = [[0] * (N + 1) for _ in range(N + 1)]
for y in range(N):
    for x in range(N):
        prefix[y + 1][x + 1] = prefix[y][x + 1] + prefix[y + 1][x] + graph[y][x] - prefix[y][x]

# output
for _ in range(M):
    y, x, ty, tx = map(int, input().split())
    print(prefix[ty][tx] - prefix[y - 1][tx] - prefix[ty][x - 1] + prefix[y - 1][x - 1])