import sys
input = sys.stdin.readline

# input
n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

# logic
left_, right_ = 0, len(arr) - 1

result = 0

while left_ < right_:
    num = arr[left_] + arr[right_]

    if num == x:
        result += 1
        left_ += 1
        right_ -=1
    elif num < x:
        left_ += 1
    else:
        right_ -= 1

print(result)
