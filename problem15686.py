import sys
from itertools import combinations

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
chickens = []
homes = []

for y in range(N):
    for x in range(N):
        if graph[y][x] == 1:
            homes.append((y, x))
        elif graph[y][x] == 2:
            chickens.append((y, x))

answer = sys.maxsize

if M == 1:
    for cy, cx in chickens:
        dis = 0
        for hy, hx in homes:
            dis += abs(hy - cy) + abs(hx - cx)
        answer = min(answer, dis)

else:
    cnt = 0
    remain_chickens = list(combinations(chickens, M))
    for hy, hx in homes:
        dis = sys.maxsize
        for cy, cx in chickens:
            dis = min(dis, abs(hy - cy) + abs(hx - cx))
        cnt += dis
    answer = min(answer, cnt)

print(answer)