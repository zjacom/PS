import copy
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
answer = 10000000

dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

directions = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

def checker(y, x):
    return y < 0 or y > N - 1 or x < 0 or x > M - 1


def move(y, x, direc, graph):
    for d in direc:
        ny, nx = y, x
        
        while True:
            nx += dx[d]
            ny += dy[d]
            if checker(ny, nx) or graph[ny][nx] == 6:
                break
            if graph[ny][nx] != 0:
                continue
            graph[ny][nx] = -1
    return graph


def init():
    cctv, answer = [], 0
    for y in range(N):
        for x in range(M):
            if arr[y][x] != 6 and arr[y][x] != 0:
                cctv.append((y, x, arr[y][x]))
            if arr[y][x] == 0:
                answer += 1
    
    return cctv, answer


cctvs, answer = init()

def cal(graph):
    global answer
    cnt = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 0:
                cnt += 1
    answer = min(answer, cnt)


def recur(idx, graph):
    if idx == len(cctvs):
        cal(graph)
        return

    # tmp = [[j for j in graph[i]] for i in range(N)]
    # tmp = copy.deepcopy(graph)
    tmp = graph[:]    

    y, x, d = cctvs[idx]

    for dir in directions[d]:
        graph = move(y, x, dir, graph)
        recur(idx + 1, graph)
        graph = tmp[:]


recur(0, arr)
print(answer)