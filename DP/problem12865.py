import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# input
N, K = map(int, input().split())
arr = [(0, 0)]
for _ in range(N):
    arr.append(list(map(int, input().split())))
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

# logic
for idx in range(1, N + 1):
    item_weight, item_value = arr[idx][0], arr[idx][1]
    for weight in range(K + 1):
        if weight < item_weight:
            dp[idx][weight] = dp[idx - 1][weight]
        else:
            dp[idx][weight] = max(dp[idx - 1][weight - arr[idx][0]] + arr[idx][1], dp[idx - 1][weight])

# output
print(max(map(max, dp)))
