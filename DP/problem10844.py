import sys
input = sys.stdin.readline

# input
# N = int(input())
# dp = [[] for _ in range(N)]
# dp[0] = [num for num in range(1, 10)]

# logic
# for i in range(1, N):
#     for num in dp[i - 1]:
#         if int(str(num)[-1]) == 9:
#             dp[i].append((num * 10 + 8) % 1_000_000_000)
#             print((num * 10 + 8) % 1_000_000_000)
#         elif int(str(num)[-1]) == 0:
#             dp[i].append((num * 10 + 1) % 1_000_000_000)
#         else:
#             dp[i].append((num * 10 + int(str(num)[-1]) - 1) % 1_000_000_000)
#             dp[i].append((num * 10 + int(str(num)[-1]) + 1) % 1_000_000_000)


# print(len(dp[N - 1]))
N = int(input())

dp = [[0] * 10 for _ in range(N + 1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1] 

print(sum(dp[N]) % 1_000_000_000)