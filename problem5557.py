N = int(input())

arr = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(101)]
dp[0][arr[0]] = 1

for n in range(len(arr) - 2):
    for num, cnt in enumerate(dp[n]):
        if cnt > 0:
            if num + arr[n + 1] <= 20:
                dp[n + 1][num + arr[n + 1]] += dp[n][num]
            if num - arr[n + 1] >= 0:
                dp[n + 1][num - arr[n + 1]] += dp[n][num]

print(dp[N - 2][arr[-1]])