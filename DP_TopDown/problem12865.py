import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# input
N, K = map(int, input().split())
arr = [(0, 0)]
for _ in range(N):
    arr.append(list(map(int, input().split())))
dp = [[0 for _ in range(100_010)] for _ in range(N + 10)]

# logic
def recur(idx, weight):
    if weight > K:
        return -sys.maxsize
    
    if idx == N + 1:
        return 0
    
    if dp[idx][weight]:
        return dp[idx][weight]
    
    dp[idx][weight] = max(recur(idx + 1, weight + arr[idx][0]) + arr[idx][1], recur(idx + 1, weight))

    return dp[idx][weight]

# output
recur(1, 0)
print(max(map(max, dp)))