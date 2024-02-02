from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

# input
V, E = map(int, input().split())
K = int(input())
graph = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# logic
q = [(0, K)]
result = [sys.maxsize] * (V + 1)
result[K] = 0

while q:
    cost, node = heapq.heappop(q)
    for v, w in graph[node]:
        if cost + w < result[v]:
            result[v] = cost + w
            heapq.heappush(q, (cost + w, v))

# output
for r in result[1:]:
    if r == sys.maxsize:
        print("INF")
    else:
        print(r)