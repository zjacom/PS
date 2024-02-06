import sys
input = sys.stdin.readline
from collections import deque

# input
N, K = map(int, input().split())

visited = [-1 for _ in range(100_001)]
visited[N] = 0

q = deque()
q.append(N)

while q:
    cx = q.popleft()
    if cx == K:
        print(visited[cx])
        break
    if 0 <= cx - 1 < 100_001 and visited[cx - 1] == -1:
        visited[cx - 1] = visited[cx] + 1
        q.append(cx - 1)
    if 0 < 2 * cx < 100_001 and visited[2 * cx] == -1:
        visited[2 * cx] = visited[cx]
        q.appendleft(2 * cx)
    if 0 <= cx + 1 < 100_001 and visited[cx + 1] == -1:
        visited[cx + 1] = visited[cx] + 1
        q.append(cx + 1)
        