import sys
input = sys.stdin.readline
from collections import deque

visited = [False] * 100_001

N, K = map(int, input().split())

visited[N] = True

q = deque([(N, [N])])
while q:
    cx, path = q.popleft()
    if cx == K:
        print(len(path))
        print(*path)
        break
    if 0 <= cx - 1 < 100_001 and not visited[cx - 1]:
        q.append((cx - 1, path + [cx - 1]))
        visited[cx - 1] = True
    if 0 <= cx + 1 < 100_001 and not visited[cx + 1]:
        q.append((cx + 1, path + [cx + 1]))
        visited[cx + 1] = True
    if 0 <= 2 * cx < 100_001 and not visited[2 * cx]:
        q.append((2 * cx, path + [2 * cx]))
        visited[2 * cx] = True