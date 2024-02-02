import sys
input = sys.stdin.readline

# input
N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] + [sys.maxsize] * N

# logic
for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = min(dp[i], dp[i - j] + arr[j])

# output
print(dp[N])