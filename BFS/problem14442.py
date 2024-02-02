from collections import deque
import sys
input = sys.stdin.readline

# 입력
N, M, K = map(int, input().split())
dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]
visited = [[[0] * (10 + 1) for _ in range(M)] for _ in range(N)]
graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip())))

# 로직
def bfs():
    global graph
    q = deque([(0, 0, 0)])
    while q:
        cy, cx, cw = q.popleft()
        if cy == N - 1 and cx == M - 1:
            return visited[cy][cx][cw]
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 1 and cw < K and not visited[ny][nx][cw + 1]:
                    visited[ny][nx][cw + 1] = visited[cy][cx][cw] + 1
                    q.append((ny, nx, cw + 1))
                if graph[ny][nx] == 0 and not visited[ny][nx][cw]:
                    visited[ny][nx][cw] = visited[cy][cx][cw] + 1
                    q.append((ny, nx, cw))

    return -1

visited[0][0][0] = 1
print(bfs())