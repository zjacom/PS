from collections import deque
import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip())))

# 로직
def bfs():
    q = deque([(0, 0, 0)])
    while q:
        cy, cx, cw = q.popleft()
        if cy == N - 1 and cx == M - 1:
            return visited[cy][cx][cw]
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                # 다음 방문할 곳이 벽이고, 벽을 부순적이 없다면
                if graph[ny][nx] == 1 and cw == 0:
                    visited[ny][nx][1] = visited[cy][cx][0] + 1
                    q.append((ny, nx, 1))
                # 다음 방문할 곳이 벽이 아니고, 방문한 적이 없다면
                if graph[ny][nx] == 0 and visited[ny][nx][cw] == 0:
                    visited[ny][nx][cw] = visited[cy][cx][cw] + 1
                    q.append((ny, nx, cw))
    return -1

visited[0][0][0] = 1
print(bfs())