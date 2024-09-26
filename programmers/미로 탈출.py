from collections import deque


def solution(maps):
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == "S":
                sy, sx = y, x
            if maps[y][x] == "L":
                ly, lx = y, x
    lever, exit = bfs(sy, sx, "L", maps), bfs(ly, lx, "E", maps)
    answer = -1
    if lever and exit:
        answer = lever + exit
    return answer


def bfs(y, x, target, maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
    q = deque([(y, x, 0)])
    while q:
        cy, cx, c = q.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and maps[ny][nx] != "X":
                    if maps[ny][nx] == target:
                        return c + 1
                    q.append((ny, nx, c + 1))
                    visited[ny][nx] = True
