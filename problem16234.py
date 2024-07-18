from collections import deque

N, L, R = map(int, input().split())

countries = [list(map(int, input().split())) for _ in range(N)]

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]


def bfs(y, x):
    path = [(y, x)]
    q = deque([(y, x)])

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                sub = abs(countries[ny][nx] - countries[cy][cx])
                if sub >= L and sub <= R:
                    q.append((ny, nx))
                    path.append((ny, nx))
                    visited[ny][nx] = 1
    if len(path) > 1:
        m = sum(countries[a][b] for a, b in path) // len(path)
        for a, b in path:
            countries[a][b] = m
        return 1
    else: return 0

result = 0
while True:
    flag = 0
    visited = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                visited[y][x] = 1
                flag += bfs(y, x)
    if not flag:
        break
    result += 1
print(result)