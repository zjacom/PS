N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())

if sum(arr) <= M:
    print(arr[-1])

left, right = 0, N - 1

while left <= right:
    mid = (left + right) // 2
    total = sum(arr[:mid]) + arr[mid] * len(arr[mid:])
    if right - left == 1:
        break
    if total < M:
        left = mid + 1
    elif total == M:
        print(arr[mid])
        break
    else:
        right = mid - 1

for num in range(arr[left] + 1, arr[left + 1]):
    total = sum(arr[:left + 1]) + num * len(arr[left + 1:])
    if total > M:
        print(num - 1)
        break
    elif total == M:
        print(num)
        break