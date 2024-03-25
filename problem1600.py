from collections import deque

K = int(input())
W, H = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(H)]

visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
hx, hy = [-1, -2, -2, -1, 1, 2, 1, 2], [-2, -1, 1, 2, -2, -1, 2, 1]

q = deque([(0, 0, 0)])
visited[0][0][0] = 1

while q:
    y, x, k = q.popleft()
    if y == H - 1 and x == W - 1:
        print(visited[y][x][k] - 1)
        exit(0)
    if k < K:
        for i in range(8):
            nhy, nhx = y + hy[i], x + hx[i]
            if 0 <= nhy < H and 0 <= nhx < W:
                if graph[nhy][nhx] == 1:
                    continue
                if not visited[nhy][nhx][k + 1]:
                    q.append((nhy, nhx, k + 1))
                    visited[nhy][nhx][k + 1] = visited[y][x][k] + 1
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < H and 0 <= nx < W:
            if graph[ny][nx] == 1:
                    continue
            if not visited[ny][nx][k]:
                q.append((ny, nx, k))
                visited[ny][nx][k] = visited[y][x][k] + 1


print(-1)