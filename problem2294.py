n, k  = map(int, input().split())

coins = sorted(list(set([int(input()) for _ in range(n)])))

dp = [10_001] * (k + 1)
dp[0] = 0
for coin in coins:
    for idx in range(coin, k + 1):
        if dp[idx] > 0:
            dp[idx] = min(dp[idx], dp[idx - coin] + 1)

print(-1) if dp[k] == 10_001 else print(dp[k])