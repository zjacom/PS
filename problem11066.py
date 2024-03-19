import sys


def file_union(K, files):
    dp = [[0] * K for _ in range(K)]

    for x in range(1, K):
        for y in range(x - 1, -1, -1):
            cost = sys.maxsize
            for k in range(x - y):
                cost = min(cost, dp[y][y + k] + dp[y + k + 1][x])
            dp[y][x] = cost + sum(files[y:x+1])
    
    return dp[0][-1]

answer = []

T = int(input())

for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))

    answer.append(file_union(K, files))

for ans in answer:
    print(ans)