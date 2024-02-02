import sys
input = sys.stdin.readline

# input
N = int(input())
arr = [[0, 0, 0]]
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(N + 1)]

# logic
for idx in range(1, N + 1):
    for color in range(3):
        dp[idx][color] = min(dp[idx - 1][(color + 1) % 3], dp[idx - 1][(color + 2) % 3]) + arr[idx][color]

# output
print(min(dp[-1]))
