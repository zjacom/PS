n, k = map(int, input().split())

coins = sorted([int(input()) for _ in range(n)])

dp = [0] * (k + 1)
dp[0] = 1

for coin in coins:
    for idx in range(coin, k + 1):
        dp[idx] += dp[idx - coin]

print(dp[-1])