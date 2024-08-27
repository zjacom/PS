from collections import deque

def bfs(graph, N):
    visited = [[-1] * N for _ in range(N)]

    q = deque([(0, 0)])
    visited[0][0] = graph[0][0]

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == -1:
                    q.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + graph[ny][nx]
                elif visited[y][x] + graph[ny][nx] < visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + graph[ny][nx]
    return visited[-1][-1]


dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
answer = []
while True:
    N = int(input())
    if N == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(N)]
    answer.append(bfs(graph, N))


for i in range(len(answer)):
    print(f"Problem {i + 1}: {answer[i]}")