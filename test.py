N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

left, right = 0, arr[-1]
total = sum(arr)
answer = 0

while left < right:
    mid = (left + right) // 2

    wood = 0
    for tree in arr:
        if mid < tree:
            wood += tree - mid
    if M == wood:
        answer = mid
        break
    elif M < wood:
        left = mid + 1
    else:
        right = mid - 1

print(answer)