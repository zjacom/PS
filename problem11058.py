N = int(input())

dp = [num for num in range(101)]

for idx in range(7, 101):
    dp[idx] = max(dp[idx - 3] * 2, dp[idx - 4] * 3, dp[idx - 5] * 4)

print(dp[N])