# 11066번
import sys

def file_union(K, arr):
    dp = [[sys.maxsize] * K for _ in range(K)]

    for i in range(K):
        dp[i][i] = 0

    for x in range(1, K):
        for y in range(x - 1, -1, -1):
            if x - y == 1:
                dp[y][x] = arr[y] + arr[x]
            else:
                cost = sys.maxsize
                for nx in range(x):
                    cost = min(cost, dp[y][nx] + dp[nx + 1][x])
                dp[y][x] = cost + sum(arr[y:x + 1])
    return dp[0][-1]

answer = []
T = int(input())
for _ in range(T):
    k = int(input())
    a = list(map(int, input().split()))

    answer.append(file_union(k, a))


for ans in answer:
    print(ans)