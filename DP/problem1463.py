import sys
input = sys.stdin.readline

# input
N = int(input())
dp = [sys.maxsize] * (N * 3 + 1)
dp[1] = 0

for i in range(1, N + 1):
    dp[i * 3] = min(dp[i * 3], dp[i] + 1)
    dp[i * 2] = min(dp[i * 2], dp[i] + 1)
    dp[i + 1] = min(dp[i + 1], dp[i] + 1)

print(dp[N])