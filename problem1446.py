import sys

N, D = map(int ,input().split())

costs = [sys.maxsize] * (D + 1)
shortcuts = []

for _ in range(N):
    shortcuts.append(list(map(int, input().split())))

costs[0] = 0

for i in range(D + 1):
    if i > 0:
        costs[i] = min(costs[i], costs[i - 1] + 1)
    for s, e, c in shortcuts:
        if i == s:
            if e <= D:
                costs[e] = min(costs[i] + c, costs[e])

print(costs[-1])