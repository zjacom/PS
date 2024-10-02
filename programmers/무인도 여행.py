from collections import deque


def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] != 'X' and not visited[y][x]:
                q = deque([(y, x)])
                cost = int(maps[y][x])
                visited[y][x] = True
                while q:
                    cy, cx = q.popleft()
                    for i in range(4):
                        ny, nx = cy + dy[i], cx + dx[i]
                        if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                            if maps[ny][nx] != 'X' and not visited[ny][nx]:
                                q.append((ny, nx))
                                cost += int(maps[ny][nx])
                                visited[ny][nx] = True
                answer.append(cost)
    return sorted(answer) if answer else [-1]