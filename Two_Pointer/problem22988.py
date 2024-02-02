import sys
input = sys.stdin.readline

# input
N, X = map(int, input().split())
arr = sorted(list(map(int, input().split())))

# logic
left_, right_ = 0, len(arr) - 1

result = 0
remain = 0

while left_ <= right_:
    if arr[right_] == X:
        result += 1
        right_ -= 1
        continue
    
    if left_ == right_:
        remain += 1
        break
    
    num = arr[left_] + arr[right_]

    if num >= X / 2:
        result += 1
        left_ += 1
        right_ -= 1
    else:
        left_ += 1
        remain += 1

print(result + remain // 3)