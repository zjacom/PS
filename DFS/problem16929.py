import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(list(input().strip()))


dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

def dfs(y, x, sy, sx, cnt):
    global visited, target
    visited[y][x] = True

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if ny == sy and nx == sx and cnt >= 4:
                print("Yes")
                exit(0)
            if not visited[ny][nx] and arr[ny][nx] == target:
                dfs(ny, nx, sy, sx, cnt + 1)
                visited[ny][nx] = False

for y in range(N):
    for x in range(M):
        visited = [[False] * M for _ in range(N)]
        target = arr[y][x]
        dfs(y, x, y, x, 1)

print("No")