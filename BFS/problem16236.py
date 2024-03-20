from collections import deque

dirY, dirX = [0, 0, 1, -1], [1, -1, 0, 0]
N = int(input())
graph = [[] * N for _ in range(N)]
shark_y, shark_x = 0, 0
for idx in range(N):
    value = list(input().split(' '))
    for jdx, v in enumerate(value):
        if v == "9":
            shark_y, shark_x = idx, jdx
            graph[idx].append(0)
        else:
            graph[idx].append(int(v))

def checker(start_y, start_x, size):
    q = deque([(start_y, start_x)])
    visited = [[0] * N for _ in range(N)]
    visited[start_y][start_x] = 1
    nxt = []
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dirY[i], x + dirX[i]
            if 0 <= ny < N and 0 <= nx < N:
                if not visited[ny][nx]:
                    if graph[ny][nx] <= size:
                        q.append((ny, nx))
                        visited[ny][nx] = 1
                        if 0 < graph[ny][nx] < size:
                            nxt.append((ny, nx))
    return nxt


def distance(start_y, start_x, point, size):
    q = deque([(start_y, start_x, 0)])
    visited = [[0] * N for _ in range(N)]
    visited[start_y][start_x] = 1
    while q:
        y, x, dis = q.popleft()
        if y == point[0] and x== point[1]:
            return dis
        for i in range(4):
            ny, nx = y + dirY[i], x + dirX[i]
            if 0 <= ny < N and 0 <= nx < N:
                if not visited[ny][nx]:
                    if graph[ny][nx] <= size:
                        q.append((ny, nx, dis + 1))
                        visited[ny][nx] = 1

nxt = checker(shark_y, shark_x, 2)
if not nxt: 
    print(0)
    exit(0)

nxt = sorted(nxt, key=lambda p : (distance(shark_y, shark_x, p, 2), p[0], p[1]))

target = nxt[0]

q = deque([(shark_y, shark_x, 2, 0, 0, [[0] * N for _ in range(N)], target)])

while q:
    y, x, size, eaten, count, visited, target = q.popleft()

    if y == target[0] and x == target[1]:
        eaten += 1
        graph[target[0]][target[1]] = 0

        if eaten == size:
            eaten = 0
            size += 1
        nxt = checker(y, x, size)
        if not nxt:
            print(count)
            exit(0)
        nxt = sorted(nxt, key=lambda p : (distance(y, x, p, size), p[0], p[1]))
        target = nxt[0]
        visited = [[0] * N for _ in range(N)]
        while q: q.pop()
        q.append((y, x, size, eaten, count, visited, target))
        continue
    
    for i in range(4):
        ny, nx = y + dirY[i], x + dirX[i]
        if 0 <= ny < N and 0 <= nx < N:
            if graph[ny][nx] <= size:
                if not visited[ny][nx]:
                    visited[ny][nx] = 1
                    q.append((ny, nx, size, eaten, count + 1, visited, target))
