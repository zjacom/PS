import sys
input = sys.stdin.readline

# input
n = int(input())
arr = []
X_max, Y_max = -sys.maxsize, -sys.maxsize
X_min, Y_min = sys.maxsize, sys.maxsize
for _ in range(n):
    x, y = map(int, input().split())
    X_max = max(X_max, x)
    X_min = min(X_min, x)
    Y_max = max(Y_max, y)
    Y_min = min(Y_min, y)
    arr.append((x, y))

# logic
X, Y = [0] * (X_max - X_min + 1), [0] * (Y_max - Y_min + 1)

for i in range(len(arr) - 1):
    if arr[i][0] != arr[i + 1][0]:# x의 좌표가 변했다면...
        if arr[i][0] < arr[i + 1][0]:
            X[arr[i][0] - X_min] += 1
            X[arr[i + 1][0] - X_min] -= 1
        else:
            X[arr[i][0] - X_min] -= 1
            X[arr[i + 1][0] - X_min] += 1
    elif arr[i][1] != arr[i + 1][1]:# y의 좌표가 변했다면...
        if arr[i][1] < arr[i + 1][1]:
            Y[arr[i][1] - Y_min] += 1
            Y[arr[i + 1][1] - Y_min] -= 1
        else:
            Y[arr[i][1] - Y_min] -= 1
            Y[arr[i + 1][1] - Y_min] += 1

# 마지막 좌표와 첫 번째 좌표를 잇는 선분도 계산
if arr[len(arr) - 1][0] != arr[0][0]:
    if arr[0][0] < arr[len(arr) - 1][0]:
        X[arr[0][0] - X_min] += 1
        X[arr[len(arr) - 1][0] - X_min] -= 1
    else:
        X[arr[0][0] - X_min] -= 1
        X[arr[len(arr) - 1][0] - X_min] += 1
elif arr[len(arr) - 1][1] != arr[0][1]:
    if arr[0][1] < arr[len(arr) - 1][1]:
        Y[arr[0][1] - Y_min] += 1
        Y[arr[len(arr) - 1][1] - Y_min] -= 1
    else:
        Y[arr[0][1] - Y_min] -= 1
        Y[arr[len(arr) - 1][1] - Y_min] += 1

# 누적합
X, Y = X[:-1], Y[:-1]
preX, preY = [0] * len(X), [0] * len(Y)
preX[0], preY[0] = X[0], Y[0]
for i in range(len(X)):
    preX[i] = max(preX[i - 1] + X[i], preX[i - 1])

for i in range(len(Y)):
    preY[i] = max(preY[i - 1] + Y[i], preY[i - 1])

# output
print(max(preX[-1], preY[-1]))