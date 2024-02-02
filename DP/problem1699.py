import sys
input = sys.stdin.readline

# input
N = int(input())
dp = [num for num in range(N + 1)]

# logic
for i in range(2, N + 1):
    for j in range(1, i):
        if j * j > i:
            break
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1

# output
print(dp)