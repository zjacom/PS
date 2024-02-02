import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**6)

# input
N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# logic
visited = [False] * N
result = 0


def dfs(node, cnt):
    global visited, result

    if cnt == 5:
        result = 1
        return

    visited[node] = True

    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt, cnt + 1)
            visited[nxt] = False


for node in range(N):
    dfs(node, 1)
    visited[node] = False
    if result == 1:
        break

# output
print(result)