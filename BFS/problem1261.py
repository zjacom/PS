from collections import deque
import sys
import heapq
input = sys.stdin.readline

# input
M, N = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().strip())))

visited = [[False] * M for _ in range(N)]
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
q = [(0, 0, 0)]
visited[0][0] = True

while q:
    ct, cy, cx = heapq.heappop(q)
    if cy == N - 1 and cx == M - 1:
        print(ct)
        break
    for i in range(4):
        ny, nx = cy + dy[i], cx + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if not visited[ny][nx]:
                if arr[ny][nx] == 0:
                    heapq.heappush(q, (ct, ny, nx))
                    visited[ny][nx] = True
                if arr[ny][nx] == 1:
                    heapq.heappush(q, (ct + 1, ny, nx))
                    visited[ny][nx] = True
