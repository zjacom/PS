import sys
input = sys.stdin.readline

# input
T = int(input())
TC = []
for _ in range(T):
    TC.append(int(input()))

# logic
dp = [[0, 0, 0] for _ in range(100_000 + 1)]
dp[1][0] = 1
dp[2][1] = 1
dp[3][0], dp[3][1], dp[3][2] = 1, 1, 1

for i in range(4, 100_000 + 1):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 1_000_000_009
    dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % 1_000_000_009
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % 1_000_000_009


# output
for c in TC:
    print(sum(dp[c]) % 1_000_000_009)


# 모듈러 연산을 두 번 하는 이유는 모듈러 분배법칙에 대해 알아보면 이해할 수 있다.