T = int(input())

answer = []
for _ in range(T):
    answer.append(int(input()))

dp = [0] * 5_001
dp[0] = 1

for idx in range(2, 5_001, 2):
    for jdx in range(2, idx + 1, 2):
        dp[idx] += dp[jdx - 2] * dp[idx - jdx]
    dp[idx] %= 1_000_000_007

for ans in answer:
    print(dp[ans])