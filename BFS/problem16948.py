from collections import deque
import sys
input = sys.stdin.readline

# 설정 및 입력
dirRC = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
N = int(input())
graph = [[-1] * N for _ in range(N)]
r1, c1, r2, c2 = map(int, input().split())
queue = deque([(r1, c1)])

# 로직
def bfs():
    while queue:
        y, x = queue.popleft()

        for dy, dx in dirRC:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and graph[ny][nx] == -1:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((ny, nx))

graph[r1][c1] = 0
bfs()
print(graph[r2][c2])