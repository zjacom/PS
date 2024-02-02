import sys
input = sys.stdin.readline

# input
N = int(input())
card = sorted(list(map(int, input().split())))
M = int(input())
arr = list(map(int, input().split()))

# logic
result = []

for num in arr:
    left, right = 0, N - 1
    flag = False

    while left <= right:
        middle = (left + right) // 2

        if card[middle] == num:
            flag = True
            break
        elif card[middle] > num:
            right = middle - 1
        elif card[middle] < num:
            left = middle + 1
    
    if flag:
        result.append(1)
    else:
        result.append(0)

print(' '.join(map(str, result)))

# right과 left에 middle - 1, middle + 1을 하는 이유는 탐색에 지장이 없고 while문을 종료시키기 위함이다.