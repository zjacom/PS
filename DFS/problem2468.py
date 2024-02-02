import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 입력
N = int(input())
graph = [[0] * (N + 10) for _ in range(N + 10)]
small, big = 101, 0
dirY, dirX = [0, 0, 1, -1], [1, -1, 0, 0]

for y in range(1, N + 1):
    value = list(map(int, input().split()))
    for x in range(N):
        small = min(small, value[x])
        big = max(big, value[x])
        graph[y][x + 1] = value[x]


def dfs(y, x, height):
    global visited, graph, dirY, dirX
    visited[y][x] = True

    for i in range(4):
        newY, newX = y + dirY[i], x + dirX[i]
        if graph[newY][newX] > height and not visited[newY][newX]:
            dfs(newY, newX, height)
    

result = 1
for height in range(small, big + 1):
    visited = [[False] * (N + 10) for _ in range(N + 10)]
    count = 0
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            if graph[y][x] <= height:
                visited[y][x] = True
    
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            if graph[y][x] > height and not visited[y][x]:
                dfs(y, x, height)
                count += 1
    
    result = max(result, count)

print(result)