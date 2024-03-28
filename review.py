# 11058번

N = int(input())

dp = [num for num in range(100 + 1)]

for idx in range(7, 100 + 1):
    dp[idx] = max(dp[idx - 5] * 4, dp[idx - 4] * 3, dp[idx - 3] * 2)

print(dp[N])