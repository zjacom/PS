import sys
from itertools import permutations

N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
spins = []
for _ in range(K):
    r, c, s = map(int, input().split())
    spins.append((r, c, s))

spins = list(permutations(spins, K))
result = sys.maxsize

def func(spin, graph):
    global result
    temp = [[n for n in graph[i]] for i in range(len(graph))]

    for r, c, s in spin:
        for ss in range(s, 0, -1):
            lu, rd = (r - ss - 1, c - ss - 1), (r + ss - 1, c + ss - 1)
            for x in range(lu[1] + 1, rd[1] + 1):
                graph[lu[0]][x] = temp[lu[0]][x - 1]
            for y in range(lu[0] + 1, rd[0] + 1):
                graph[y][rd[1]] = temp[y - 1][rd[1]]
            for x in range(rd[1] - 1, lu[1] - 1, -1):
                graph[rd[0]][x] = temp[rd[0]][x + 1]
            for y in range(rd[0] - 1, lu[0] - 1, -1):
                graph[y][lu[1]] = temp[y + 1][lu[1]]
            
        temp = [[n for n in graph[i]] for i in range(len(graph))]

    for row in graph:
        result = min(result, sum(row))
        
for spin in spins:
    temp = [[n for n in graph[i]] for i in range(len(graph))]
    func(spin, temp)

print(result)