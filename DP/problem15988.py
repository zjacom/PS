import sys
input = sys.stdin.readline

# input
T = int(input())
TC = []
for _ in range(T):
    n = int(input())
    TC.append(n)
dp = [0] * 1_000_001
dp[1], dp[2], dp[3] = 1, 2, 4

# logic
for idx in range(4, 1_000_001):
    dp[idx] = ((dp[idx - 1] + dp[idx - 2] + dp[idx - 3]) % 1_000_000_009)

# output
for c in TC:
    print(dp[c])