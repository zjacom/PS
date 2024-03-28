# 2294번
import sys

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [-1] * (k + 1)
dp[0] = 0

for idx in range(1, k + 1):
    mini = sys.maxsize
    for coin in coins:
        if idx - coin >= 0 and dp[idx -coin] != -1:
            mini = min(mini, dp[idx - coin] + 1)
    if mini != sys.maxsize:
        dp[idx] = mini

print(dp[-1])