import sys

N = int(input())
dis = list(map(int, input().split()))
costs = list(map(int, input().split()))

mini = sys.maxsize
result = 0
for i in range(N - 1):
    mini = min(mini, costs[i])
    result += mini * dis[i]

print(result)