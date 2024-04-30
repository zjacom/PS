import sys
from itertools import combinations

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

homes, chickens = [], []
answer = sys.maxsize

for y in range(N):
    for x in range(N):
        if graph[y][x] == 1:
            homes.append((y, x))
        elif graph[y][x] == 2:
            chickens.append((y, x))

if M == 1:
    for cy, cx in chickens:
        temp = 0
        for hy, hx in homes:
            temp += (abs(cy - hy) + abs(cx - hx))
        answer = min(answer, temp)

else:
    chickens = list(combinations(chickens, M))
    for selected_chickens in chickens:
        temp1 = 0
        for hy, hx in homes:
            temp = sys.maxsize
            for cy, cx in selected_chickens:
                temp = min(temp, abs(hy - cy) + abs(hx - cx))
            temp1 += temp
        answer = min(answer, temp1)

print(answer)