import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY, dirX = [1, -1, 0, 0], [0, 0, 1, -1]
graph = []

# input
M, N = map(int, input().split()) # M이 세로, N이 가로
for _ in range(M):
    graph.append(list(map(int, input().split())))

dp = [[-1] * N for _ in range(M)]
result = 0

# logic
def recur(y, x):
    if y == M - 1 and x == N - 1:
        return 1
    
    if dp[y][x] != -1: return dp[y][x]
    
    cnt = 0
    for i in range(4):
        ny, nx = y + dirY[i], x + dirX[i]
        if 0 <= ny < M and 0 <= nx < N:
            if graph[ny][nx] < graph[y][x]:
                cnt += recur(ny, nx)

    dp[y][x] = cnt
    return dp[y][x]

recur(0, 0)
print(dp[0][0])