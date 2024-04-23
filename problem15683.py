import copy
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
answer = 10000000

d_one = [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]]
d_two = [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]]
d_three = [[(0, 1), (0, -1)], [(0, 1), (-1, 0)], [(0, -1), (1, 0)], [(0, -1), (-1, 0)]]
d_four = [[(0, 1), (-1, 0), (0, -1)], [(0, 1), (-1, 0), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (-1, 0), (0, -1)]]
d_five = [[(0, 1), (1, 0), (-1, 0), (0, -1)]]


def checker(y, x, dy, dx, graph):
    a = 1
    while True:
        ny, nx = y + (dy * a), x + (dx * a)
        if 0 > ny or ny >= N or 0 or nx >= M or nx < 0:
            break
        if graph[ny][nx] == 0:
            graph[ny][nx] = -1
            a += 1
        elif graph[ny][nx] == 6:
            break
        else:
            a += 1
    return graph


def recur(graph):
    global answer
    cnt = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 0:
                cnt += 1
    answer = min(answer, cnt)

    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                graph[y][x] = -1
                for d in d_one:
                    for dy, dx in d:
                        g = checker(y, x, dy, dx, copy.deepcopy(graph))
                        recur(g)
            elif graph[y][x] == 2:
                graph[y][x] = -1
                for d in d_two:
                    for dy, dx in d:
                        g = checker(y, x, dy, dx, copy.deepcopy(graph))
                        recur(g)
            elif graph[y][x] == 3:
                graph[y][x] = -1
                for d in d_three:
                    for dy, dx in d:
                        g = checker(y, x, dy, dx, copy.deepcopy(graph))
                        recur(g)
            elif graph[y][x] == 4:
                graph[y][x] = -1
                for d in d_four:
                    for dy, dx in d:
                        g = checker(y, x, dy, dx, copy.deepcopy(graph))
                        recur(g)
            elif graph[y][x] == 5:
                graph[y][x] = -1
                for d in d_five:
                    for dy, dx in d:
                        g = checker(y, x, dy, dx, copy.deepcopy(graph))
                        recur(g)
recur(arr)
print(answer)