from collections import deque
import sys
input = sys.stdin.readline

# 입력
N, M, K = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip())))

visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

# 로직
def bfs():
    global visited, graph
    q = deque([(0, 0, 0, 1, 0)])
    while q:
        cy, cx, cw, cd, ct = q.popleft()
        if cy == N - 1 and cx == M - 1:
            return cd
        
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < N and 0 <= nx < M: # 다음 행선지로 이동할 수 있음
                if graph[ny][nx] == 1 and cw < K: # 다음 행선지가 벽이고 벽을 뚫을 수 있다면
                    if visited[ny][nx][cw + 1] == 0: # 다음 행선지를 방문할 수 있다면
                        if ct == 0: # 낮이라면 다음 행선지 방문 처리 후, 경로 1 증가
                            visited[ny][nx][cw + 1] = 1
                            q.append((ny, nx, cw + 1, cd + 1, 1))
                        else: # 밤이라면
                            q.append((cy, cx, cw, cd + 1, 0))
                if graph[ny][nx] == 0: # 다음 행선지가 벽이 아니라면
                    if visited[ny][nx][cw] == 0: # 방문 여부 체크
                        if ct == 0: # 낮이라면
                            visited[ny][nx][cw] = visited[cy][cx][cw] + 1
                            q.append((ny, nx, cw, cd + 1, 1))
                        else: # 밤이라면
                            visited[ny][nx][cw] = visited[cy][cx][cw] + 1
                            q.append((ny, nx, cw, cd + 1, 0))
    return -1


# 출력
visited[0][0][0] = 1
print(bfs())
