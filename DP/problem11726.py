import sys
input = sys.stdin.readline

# input 
N = int(input())
dp = [0 for _ in range(N + 10)]
dp[0] = 1
dp[1] = 1

# logic
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

# output
if N == 1:
    print(1)
else: print(dp[N] % 10_007)
