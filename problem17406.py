import sys
from itertools import permutations

N, M, K = map(int, input().split())

AAA = [list(map(int, input().split())) for _ in range(N)]
spins = []

for _ in range(K):
    a, b, c = map(int, input().split())
    spins.append((a, b, c))


def func(p1, p2, graph):
    lu, ld, ru, rd = (p1[0], p1[1]), (p2[0], p1[1]), (p1[0], p2[1]), (p2[0], p2[1])

    arr = [[n for n in graph[i]] for i in range(N)]

    HHH, A, B = lu[0], lu[1] + 1, ru[1]
    while B - A > 0:
        for x in range(A, B):
            arr[HHH][x] = graph[HHH][x - 1]
        A += 1
        B -= 1
        HHH += 1
    
    HH, C, D = ld[0], ld[1] + 1, rd[1]
    while D - C > 0:
        for x in range(C, D):
            arr[HH][x] = graph[HH][x + 1]
        C += 1
        D -= 1
        HH -= 1
    
    WW, E, F = lu[1], lu[0] + 1, ld[0]
    while F - E > 0:
        for y in range(E, F):
            arr[y][WW] = graph[y + 1][WW]
        E += 1
        F -= 1
        WW += 1
    
    WWW, G, H = ru[1], ru[0] + 1, rd[0]
    while H - G > 0:
        for y in range(G, H):
            arr[y][WWW] = graph[y - 1][WWW]
        G += 1
        H -= 1
        WWW -= 1
    
    while lu != ld != ru != rd:
        arr[lu[0]][lu[1]] = graph[lu[0] + 1][lu[1]]
        arr[ru[0]][ru[1]] = graph[ru[0]][ru[1] - 1]
        arr[ld[0]][ld[1]] = graph[ld[0]][ld[1] + 1]
        arr[rd[0]][rd[1]] = graph[rd[0] - 1][rd[1]]

        lu = (lu[0] + 1, lu[1] + 1)
        ru = (ru[0] + 1, ru[1] - 1)
        ld = (ld[0] - 1, ld[1] + 1)
        rd = (rd[0] - 1, rd[1] - 1)
    
    return arr


def calculator(arr):
    total = sys.maxsize
    for y in range(N):
        total = min(total, sum(arr[y]))
    
    return total


if K == 1:
    result = func((spins[0][0] - spins[0][2] - 1, spins[0][1] - spins[0][2] - 1), (spins[0][0] + spins[0][2] - 1, spins[0][1] + spins[0][2] - 1), AAA)
    answer = calculator(result)
    print(answer)
else:
    answer = sys.maxsize
    for order in list(permutations(spins, K)):
        result = [[n for n in AAA[i]] for i in range(N)]
        for i in range(len(order)):
            p1, p2 = (order[i][0] - order[i][2] - 1, order[i][1] - order[i][2] - 1), (order[i][0] + order[i][2] - 1, order[i][1] + order[i][2] - 1)
            result = func(p1, p2, result)
        answer = min(answer, calculator(result))

print(answer)