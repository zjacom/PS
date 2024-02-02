import sys
input = sys.stdin.readline
from collections import deque

# input
TC = int(input())
arr = []
for _ in range(TC):
    i = int(input())
    sy, sx = map(int, input().split())
    fy, fx = map(int, input().split())
    arr.append((i, (sy, sx), (fy, fx)))

# logic
dy, dx = [-2, -2, 2, 2, -1, -1, 1, 1], [1, -1, 1, -1, 2, -2, 2, -2]

def bfs(y, x):
    global I, ty, tx, visited
    q = deque([(y, x, 0)])
    while q:
        cy, cx, cc = q.popleft()
        if cy == ty and cx == tx:
            return cc
        for i in range(8):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < I and 0 <= nx < I:
                if not visited[ny][nx]:
                    q.append((ny, nx, cc + 1))
                    visited[ny][nx] = True

# output
for c in arr:
    I = c[0]
    ty, tx = c[2][0], c[2][1]
    visited = [[False] * I for _ in range(I)]
    visited[c[1][0]][c[1][1]] = True
    print(bfs(c[1][0], c[1][1]))