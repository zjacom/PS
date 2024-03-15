N, M = map(int, input().split())

graph = [[0 for _ in range(M + 1)]]
for i in range(1, N + 1):
    graph.append([0] + list(map(int, input().split())))

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] ) + graph[i][j]


print(dp[N][M])