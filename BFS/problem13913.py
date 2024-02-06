import sys
input = sys.stdin.readline
from collections import deque

visited = [-1] * 100_001

N, K = map(int, input().split())

visited[N] = N

q = deque([(N, 0)])
path = []
while q:
    cx, cnt = q.popleft()
    if cx == K:
        print(cnt)
        while cx != N:
            path.append(cx)
            cx = visited[cx]
        break
    if 0 <= cx - 1 and visited[cx - 1] == -1:
        q.append((cx - 1, cnt + 1))
        visited[cx - 1] = cx
    if 0 < cx + 1 < 100_001 and visited[cx + 1] == -1:
        q.append((cx + 1, cnt + 1))
        visited[cx + 1] = cx
    if 0 < 2 * cx < 100_001 and visited[2 * cx] == -1:
        q.append((2 * cx, cnt + 1))
        visited[2 * cx] = cx

path += [N]
print(*path[::-1])