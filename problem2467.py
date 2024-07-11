import sys

N = int(input())

arr = list(map(int, input().split()))

left, right = 0, N - 1

var = sys.maxsize
answer = []

while left < right:
    sumi = arr[right] + arr[left]
    if var > abs(sumi):
        answer = [arr[left], arr[right]]
        var = abs(sumi)
    
    if sumi < 0:
        left += 1
    elif sumi > 0:
        right -= 1
    else:
        break

print(*answer)