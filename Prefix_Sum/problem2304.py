import sys
input = sys.stdin.readline

# input
N = int(input())
arr = []

for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

# logic
arr.sort(key=lambda x: x[0])
mx, my = max(arr, key=lambda x: x[1])

left_mi, right_mi = 0, 0
for i in range(N):
    if arr[i] == (mx, my):
        left_mi = i

for i in range(N - 1, -1, -1):
    if arr[i] == (mx, my):
        right_mi = i

left_sx, left_sy = arr[0][0], arr[0][1]
right_sx, right_sy = arr[-1][0], arr[-1][1]
left_sum, right_sum = 0, 0

for i in range(1, left_mi + 1):
    if left_sy >= arr[i][1]:
        continue
    else:
        left_sum += (my - left_sy) * (arr[i][0] - left_sx)
        left_sx, left_sy = arr[i][0], arr[i][1]

for i in range(N - 2, right_mi -1 , -1):
    if right_sy >= arr[i][1]:
        continue
    else:
        right_sum += (my - right_sy) * abs(arr[i][0] - right_sx)
        right_sx, right_sy = arr[i][0], arr[i][1]

total = my * (arr[-1][0] - arr[0][0] + 1)

# ouput
print(total - left_sum - right_sum)