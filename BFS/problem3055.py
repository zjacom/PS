from collections import deque
import sys
input = sys.stdin.readline

# 입력
R, C = map(int, input().split())
s, e, water = 0, 0, deque()
graph = [[] for _ in range(R)]
for y in range(R):
    value = input().strip()
    for x, v in enumerate(value):
        graph[y].append(v)
        if v == "S":
            s = (y, x, 0)
        if v == "D":
            e = (y, x)
        if v == "*":
            water.append((y, x))

visited = [[False] * C for _ in range(R)]
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]


def func(y, x):
    global graph
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < R and 0 <= nx < C:
            if graph[ny][nx] == "*":
                return False
    return True


# 로직
def bfs():
    global graph, visited
    q = deque([s])
    while q:
        for _ in range(len(q)):
            cy, cx, cd = q.popleft()
            if cy == e[0] and cx == e[1]:
                return cd
            for i in range(4):
                ny, nx = cy + dy[i], cx + dx[i]
                if 0 <= ny < R and 0 <= nx < C:
                    if graph[ny][nx] == "D":
                        q.append((ny, nx, cd + 1))
                        continue
                    if graph[ny][nx] != "X" and graph[ny][nx] != "*":
                        if func(ny, nx) and not visited[ny][nx]:
                            q.append((ny, nx, cd + 1))
                            visited[ny][nx] = True

        for _ in range(len(water)):
            wy, wx = water.popleft()
            for i in range(4):
                nwy, nwx = wy + dy[i], wx + dx[i]
                if 0 <= nwy < R and 0 <= nwx < C and graph[nwy][nwx] == ".":
                    graph[nwy][nwx] = "*"
                    water.append((nwy, nwx))

    return "KAKTUS"

# 출력
visited[s[0]][s[1]] = True
print(bfs())
