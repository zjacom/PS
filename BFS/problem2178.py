from collections import deque
import sys
input = sys.stdin.readline
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

# 입력
N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

# 로직
def bfs(y, x):
    global answer, graph

    q = deque([(y, x)])
    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 1:
                    q.append((ny, nx))
                    graph[ny][nx] = graph[cy][cx] + 1
# 출력
bfs(0, 0)
print(graph[N - 1][M - 1])