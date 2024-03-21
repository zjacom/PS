str1, str2 = input().strip(), input()

dp = [[0] * 4_001 for _ in range(4_001)]
maxi = 0

for y in range(1, len(str1) + 1):
    for x in range(1, len(str2) + 1):
        if str1[y - 1] == str2[x - 1]:
            dp[y][x] = dp[y - 1][x - 1] + 1
            maxi = max(maxi, dp[y][x])

print(maxi)