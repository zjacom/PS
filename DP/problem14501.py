import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# input
N = int(input())
arr = [0]
for _ in range(N):
    arr.append(list(map(int, input().split())))
dp = [0 for _ in range(N + 10)]

# logic
for idx in range(N, 0, -1):
    if idx + arr[idx][0] > N + 1:
        dp[idx] = dp[idx + 1]
    else:
        dp[idx] = max(dp[idx + arr[idx][0]] + arr[idx][1], dp[idx + 1])
# output
print(max(dp))
