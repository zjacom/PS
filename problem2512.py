N = int(input())
arr = list(map(int, input().split()))
M = int(input())

left, right = 0, max(arr)

while left <= right:
    mid = (left + right) // 2
    total = 0
    for num in arr:
        if num < mid:
            total += num
        else:
            total += mid
    
    if total <= M:
        left = mid + 1
    else:
        right = mid - 1

print(right)