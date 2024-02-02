import sys
input = sys.stdin.readline

# input
A = int(input())
arr = list(map(int, input().split()))
dp = [1] * A

for i in range(1, A):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

maxi = max(dp)
print(maxi)

result = []
for i in range(len(dp) - 1, -1, -1):
    if dp[i] == maxi:
        result.append(arr[i])
        maxi -= 1

# print(' '.join(map(str, result[::-1])))
print(*result[::-1])

# 배열을 한 칸씩 띄어서 출력할 때 조인보다 *를 사용하는 것이 더 간단하다.