from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 입력
N = int(input())
graph = [[0] * (N + 10) for _ in range(N + 10)]

for column in range(1, N + 1):
    value = input()
    for row, v in enumerate(value):
        if v == "1":
            graph[column][row] = "1"

# 로직
dirX = [1, -1, 0, 0]
dirY = [0, 0, 1, -1]

def dfs(y, x):
    global graph, small_count
    if graph[y][x] != "1":
        return
    else:
        graph[y][x] = "v"
        small_count += 1

    for i in range(4):
        dfs(y + dirY[i], x + dirX[i])

big_count = 0
small = []
for y in range(len(graph)):
    for x in range(len(graph[0])):
        if graph[y][x] == "1":
            small_count = 0
            dfs(y, x)
            small.append(small_count)
            big_count += 1

print(big_count)
for s in sorted(small):
    print(s)
