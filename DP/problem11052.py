import sys
input = sys.stdin.readline

# input
N = int(input())
arr = [0] + list(map(int, input().split()))

# logic
dp = arr[:]

for i in range(2, N + 1):
    for j in range(1, i // 2 + 1):
        dp[i] = max(dp[i], dp[i - j] + dp[j])

# output
print(dp[-1])