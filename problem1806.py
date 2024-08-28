N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
result = 100001
prefix = arr[left]

while True:
    if prefix < S:
        right += 1
        if right >= N:
            break
        prefix += arr[right]
    else:
        result = min(result, right - left + 1)
        prefix -= arr[left]
        left += 1

if result == 100001:
    print(0)
else:
    print(result)