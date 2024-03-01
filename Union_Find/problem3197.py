import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())

dirY, dirX = [0, 0, 1, -1], [1, -1, 0, 0]

graph = [list(input().strip()) for _ in range(R)]
parents = [[(y, x) for x in range(C)] for y in range(R)]
rank = [[0] * C for _ in range(R)]
visited = [[0] * C for _ in range(R)]
swans = []

# Union-Find
def find(y, x):
    if parents[y][x] != (y, x):
        parents[y][x] = find(parents[y][x][0], parents[y][x][1])
    return parents[y][x]

def union(a, b):
    a = find(a[0], a[1])
    b = find(b[0], b[1])

    if rank[a[0]][a[1]] < rank[b[0]][b[1]]:
        parents[b[0]][b[1]] = a
    elif rank[a[0]][a[1]] > rank[b[0]][b[1]]:
        parents[a[0]][a[1]] = b
    else:
        parents[b[0]][b[1]] = a
        rank[a[0]][a[1]] += 1

# 백조의 위치를 파악하고 graph에서 백조를 "."으로 변경
for y in range(R):
    for x in range(C):
        if graph[y][x] == "L":
            swans.append((y, x))
            graph[y][x] = "."
            if len(swans) == 2:
                break

melt = deque()
for y in range(R):
    for x in range(C):
        if graph[y][x] == "." and not visited[y][x]:
            q = deque([(y, x)])
            visited[y][x] = 1
            while q:
                cy, cx = q.popleft()
                parents[cy][cx] = (y, x)
                for i in range(4):
                    ny, nx = cy + dirY[i], cx + dirX[i]
                    if 0 <= ny < R and 0 <= nx < C:
                        if graph[ny][nx] == "." and not visited[ny][nx]:
                            q.append((ny, nx))
                            visited[ny][nx] = 1
                        elif graph[ny][nx] == "X" and not visited[ny][nx]:
                            melt.append((ny, nx))
                            visited[ny][nx] = 1

answer = 0
while find(swans[0][0], swans[0][1]) != find(swans[1][0], swans[1][1]):
    temp = deque()
    while melt:
        y, x = melt.popleft()
        graph[y][x] = "."
        union_point = []
        for i in range(4):
            ny, nx = y + dirY[i], x + dirX[i]
            if 0 <= ny < R and 0 <= nx < C:
                if graph[ny][nx] == "X" and not visited[ny][nx]:
                    temp.append((ny, nx))
                    visited[ny][nx] = 1
                elif graph[ny][nx] == ".":
                    union_point.append((ny, nx))
        for point in union_point:
            if find(point[0], point[1]) != find(y, x):
                union(point, (y, x))
    melt = temp
    answer += 1

print(answer)