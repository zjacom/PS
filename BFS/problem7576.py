from collections import deque
import sys
input = sys.stdin.readline
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

# 입력 및 설정
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
q = deque()
answer = 0

for y in range(N):
    for x in range(M):
        if graph[y][x] == 1:
            q.append((y, x))


# 로직
def bfs():
    global graph, q

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[cy][cx] + 1
                    q.append((ny, nx)) 

# 로직 실행 및 출력
bfs()
for row in graph:
    if 0 in row:
        print(-1)
        exit(0)
    answer = max(answer, max(row))
print(answer - 1)
