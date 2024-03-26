# 10422번

T = int(input())
answer = [int(input()) for _ in range(T)]

dp = [0] * 5001
dp[0] = 1

for idx in range(2, 5001, 2):
    for jdx in range(2, idx + 1, 2):
        dp[idx] += dp[idx - jdx] * dp[jdx - 2]
    dp[idx] = dp[idx] % 1_000_000_007

for ans in answer:
    print(dp[ans])
