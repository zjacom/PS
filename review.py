# 17406번
from itertools import permutations
import sys

N, M, K = map(int ,input().split())
temp = [list(map(int, input().split())) for _ in range(N)]
orders = [list(map(int, input().split())) for _ in range(K)]


def func(y1, x1, y2, x2, g):
    copied_graph = [[n for n in row] for row in g]
    
    a = 1
    while y1 + x1 < y2 + x2:
        for x in range(x1 + 1, x2 + 1):
            copied_graph[y1][x] = graph[y1][x - 1]
        for y in range(y1 + 1, y2 + 1):
            copied_graph[y][x2] = graph[y - 1][x2]
        for x in range(x2 - 1, x1 - 1, -1):
            copied_graph[y2][x] = graph[y2][x + 1]
        for y in range(y2 - 1, y1 - 1, -1):
            copied_graph[y][x1] = graph[y + 1][x1]
        y1, x1, y2, x2 = y1 + a, x1 + a, y2 - a, x2 - a
    
    return copied_graph

result = sys.maxsize

for o in list(permutations(orders, K)):
    graph = [[n for n in row] for row in temp]
    for order in o:
        graph = func(order[0] - order[2] - 1, order[1] - order[2] - 1, order[0] + order[2] - 1, order[1] + order[2] - 1, graph)
    for row in graph:
        result = min(sum(row), result)
print(result)