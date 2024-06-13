from collections import deque
import sys

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

mini = sys.maxsize

dx = [-1, 0, 1]

def bfs(y, x):
    total = sys.maxsize
    q = deque([(y, x, 0, -1)])

    while q:
        cy, cx, cost, d = q.popleft()
        if cy == N:
            total = min(total, cost)
        
        for i in range(3):
            if d != i:
                ny, nx = cy + 1, cx + dx[i]
                if ny <= N and 0 <= nx < M:
                    q.append((ny, nx, cost + graph[cy][cx], i))
    return total


for x in range(M):
    mini = min(mini, bfs(0, x))

print(mini)