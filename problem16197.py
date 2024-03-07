import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(input()) for _ in range(N)]
coins = []
dirY, dirX = [0, 0, 1, -1], [1, -1, 0, 0]
answer = sys.maxsize

for y in range(N):
    for x in range(M):
        if graph[y][x] == "o":
            coins.append((y, x))
            graph[y][x] = "."
            if len(coins) == 2:
                break


def recur(y1, x1, y2, x2, count):
    global answer
    if count > 10:
        return
    
    for i in range(4):
        ny1, nx1 = y1 + dirY[i], x1 + dirX[i]
        ny2, nx2 = y2 + dirY[i], x2 + dirX[i]
        if ny1 < 0 or ny1 >= N or nx1 < 0 or nx1 >= M:
            if 0 <= ny2 < N and 0 <= nx2 < M:
                answer = min(answer, count + 1)
                return
        elif ny2 < 0 or ny2 >= N or nx2 < 0 or nx2 >= M:
            if 0 <= ny1 < N and 0 <= nx1 < M:
                answer = min(answer, count + 1)
                return
        if 0 <= ny1 < N and 0 <= nx1 < M and 0 <= ny2 < N and 0 <= nx2 < M:
            if graph[ny1][nx1] == "#" and graph[ny2][nx2] == "#":
                recur(y1, x1, y2, x2, count + 1)
            elif graph[ny1][nx1] == "#":
                recur(y1, x1, ny2, nx2, count + 1)
            elif graph[ny2][nx2] == "#":
                recur(ny1, nx1, y2, x2, count + 1)
            else:
                recur(ny1, nx1, ny2, nx2, count + 1)


recur(coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0)
print(-1) if answer > 10 else print(answer)