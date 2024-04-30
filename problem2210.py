from collections import deque

graph = [list(input().split()) for _ in range(5)]
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
result = set()


def func(y, x):
    global result

    q = deque([(y, x, graph[y][x], 5)])

    while q:
        cy, cx, s, cnt = q.popleft()
        if cnt == 0:
            result.add(s)
            continue
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5:
                q.append((ny, nx, s + graph[ny][nx], cnt - 1))


for y in range(5):
    for x in range(5):
        func(y, x)

print(len(result))