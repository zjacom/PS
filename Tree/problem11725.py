import sys
from collections import defaultdict
input = sys.stdin.readline

# input
N = int(input())
graph = defaultdict(list)
for _ in range(N - 1):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

result = [0 for _ in range(N + 1)]
_child = [0 for _ in range(N + 1)]

# logic
def recur(node, prev):
    global result, graph

    result[node] = prev

    for nxt in graph[node]:
        if nxt == prev:
            continue
        recur(nxt, node)
        _child[node] += 1

# output
recur(1, 0)
for node in result[2:]:
    print(node)

print(_child)