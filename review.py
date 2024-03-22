# 백준 11048번 복습
N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (M) for _ in range(N)]

dp[0][0] = graph[0][0]

for x in range(1, M):
    dp[0][x] = dp[0][x - 1] + graph[0][x]

for y in range(1, N):
    dp[y][0] = dp[y - 1][0] + graph[y][0]

for y in range(1, N):
    for x in range(1, M):
        dp[y][x] = max(dp[y - 1][x - 1], dp[y][x - 1], dp[y - 1][x]) + graph[y][x]

print(dp[N - 1][M - 1])