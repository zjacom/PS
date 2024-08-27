N = int(input())

arr = sorted(list(map(int, input().split())))
count = 0

for i in range(N):
    left, right = 0, N - 1
    while left < right:
        if left == i:
            left += 1
        elif right == i:
            right -= 1
        elif arr[left] + arr[right] > arr[i]:
            right -= 1
        elif arr[left] + arr[right] < arr[i]:
            left += 1
        elif arr[left] + arr[right] == arr[i]:
            count += 1
            break

print(count)
