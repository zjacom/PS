import sys

N = int(input())
buildings = list(map(int, input().split()))

dp = [[] for _ in range(N)]

stack = []
for i, h in enumerate(buildings):
    while stack and stack[-1][1] <= h:
        stack.pop()
    
    for s in stack:
        dp[i].append(s)

    stack.append([i, h])

stack = []
for i, h in reversed(list(enumerate(buildings))):
    while stack and stack[-1][1] <= h:
        stack.pop()
    
    for s in stack:
        dp[i].append(s)

    stack.append([i, h])


for i, v in enumerate(dp):
    if not v:
        print(0)
    else:
        v = sorted(v, key=lambda x: abs(i - x[0]))
        print(len(v), v[0][0] + 1)
