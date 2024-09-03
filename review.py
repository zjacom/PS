# 1253번

N = int(input())
arr = sorted(list(map(int, input().split())))
result = 0

for i in range(N):
    left, right = 0, N - 1
    while left < right:
        s = arr[left] + arr[right]
        if left == i:
            left += 1
        elif right == i:
            right -= 1
        elif s == arr[i]:
            result += 1
            break
        elif s < arr[i]:
            left += 1
        else:
            right -= 1

print(result)