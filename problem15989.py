n = int(input())

answer = []
for _ in range(n):
    answer.append(int(input()))

dp = [[0] * 10_001 for _ in range(3)]
dp[0][1], dp[0][2], dp[1][2] = 1, 1, 1
dp[0][3], dp[2][3] = 2, 1

for num in range(4, 10_001):
    dp[0][num] = dp[0][num - 1] + dp[1][num - 1] + dp[2][num - 1]
    dp[1][num] = dp[1][num - 2] + dp[2][num - 2]
    dp[2][num] = dp[2][num - 3]

for num in answer:
    print(dp[0][num] + dp[1][num] + dp[2][num])