from itertools import combinations

H, W = map(int, input().split())

N = int(input())

arr = []

for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

com = list(combinations(arr, 2))


def checker(y, x):
    temp = []

    if H >= y and W >= x:
        temp.append((y, W - x))
        temp.append((H - y, W))
    if H >= x and W >= y:
        temp.append((x, W - y))
        temp.append((H - x, W))

    return temp


answer = 0

for a, b in com:
    for li in checker(a[0], a[1]):
        if li[0] >= b[0] and li[1] >= b[1]:
            answer = max(answer, a[0] * a[1] + b[0] * b[1])
        elif li[0] >= b[1] and li[1] >= b[0]:
            answer = max(answer, a[0] * a[1] + b[0] * b[1])
    for li in checker(b[0], b[1]):
        if li[0] >= a[0] and li[1] >= a[1]:
            answer = max(answer, a[0] * a[1] + b[0] * b[1])
        elif li[0] >= a[1] and li[1] >= a[0]:
            answer = max(answer, a[0] * a[1] + b[0] * b[1])

print(answer)