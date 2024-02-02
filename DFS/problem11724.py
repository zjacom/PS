import sys
import collections
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

dic = collections.defaultdict(list)
visited = [False] * (N + 1)
result = 0

for _ in range(M):
    x, y = map(int, input().split())
    dic[x].append(y)
    dic[y].append(x)


def dfs(node):
    global visited, dic
    visited[node] = True

    for n in dic[node]:
        if not visited[n]:
            dfs(n)


for node in range(1, N + 1):
    if not visited[node]:
        dfs(node)
        result += 1

print(result)
