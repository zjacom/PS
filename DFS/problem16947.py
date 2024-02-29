from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())

graph = defaultdict(list)

for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

arr = [0] * (N + 1)
circle = []


visited = [False] * (N + 1)
def find_circle(node, path, start, cnt):
    global circle, visited
    visited[node] = True

    for nxt in graph[node]:
        if nxt == start and cnt >= 3:
            circle = path[:]
            return
        if not visited[nxt]:
            find_circle(nxt, path + [nxt], start, cnt + 1)
            visited[nxt] = False

for node in range(1, N + 1):
    find_circle(node, [node], node, 1)
    visited[node] = False
    if circle:
        break

answer = []
def dfs(node, cnt):
    if node in circle:
        answer.append(cnt)
        return
    
    visited[node] = True
    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt, cnt + 1)
            visited[nxt] = False

for node in range(1, N + 1):
    dfs(node, 0)
    visited[node] = False

print(*answer)