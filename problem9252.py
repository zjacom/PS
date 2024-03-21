str1 = input().strip()
str2 = input()

dp = [[''] * (1000 + 1) for _ in range(1000 + 1)]

for y in range(1, len(str1) + 1):
    for x in range(1, len(str2) + 1):
        if str1[y - 1] == str2[x - 1]:
            dp[y][x] = dp[y - 1][x - 1] + str1[y - 1]
        else:
            dp[y][x] = max(dp[y - 1][x], dp[y][x - 1], key=len)

if dp[len(str1)][len(str2)]:
    print(len(dp[len(str1)][len(str2)]))
    print(dp[len(str1)][len(str2)])
else:
    print(0)