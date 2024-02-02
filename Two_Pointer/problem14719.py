from collections import deque
import sys
input = sys.stdin.readline

# input
H, W = map(int, input().split())
arr = list(map(int, input().split()))

# logic
result = 0
left, right = 0, W - 1
mid, temp = 0, -1
for i, v in enumerate(arr):
    if temp < v:
        mid = i
        temp = v
left_maxi, right_maxi = 0, 0

while left < right:
    if left < mid:
        left_maxi = max(left_maxi, arr[left])
        result += left_maxi - arr[left]
        left += 1
    if mid < right:
        right_maxi = max(right_maxi, arr[right])
        result += right_maxi - arr[right]
        right -= 1

# output
print(result)