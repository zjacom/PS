import sys
input = sys.stdin.readline

# input
T = int(input())
arr = []
for _ in range(T):
    arr.append(int(input()))

# logic
dp = [1] * (10 + 1)
dp[2] = 2

for i in range(3, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

# output
for n in arr:
    print(dp[n])