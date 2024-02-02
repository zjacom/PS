import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# logic
left, right = 1, max(arr)

while left <= right:
    mid = (left + right) // 2

    wood = 0
    for tree in arr:
        if tree > mid:
            wood += tree - mid
    
    if wood >= M:
        left = mid + 1
    else:
        right = mid -1

print(right)

# 처음부터 못 푼 이유
        # arr에 있는 나무의 길이 중 하나를 높이의 기준으로 잡음.
        # 사실은 그럴 필요 없고 그냥 1부터 최대 나무의 길이까지로 범위를 잡아서, 이분 탐색을 진행하면 됨.