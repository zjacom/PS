import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dirY, dirX = [0, 0, 1, -1], [1, -1, 0, 0]

# 입력
M, N, K = map(int, input().split())
graph = [[False] * (N) for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(M - y2, M - y1):
        for x in range(N - x2, N - x1):
            graph[y][x] = True
            
# 로직
def dfs(y, x):
    global graph, a
    graph[y][x] = True
    a += 1

    for i in range(4):
        newY, newX = y + dirY[i], x + dirX[i]
        if 0 <= newY <= M - 1 and 0 <= newX <= N - 1 and not graph[newY][newX]:
            dfs(newY, newX)
    
# 실행
count = 0
result = []
for y in range(M):
    for x in range(N):
        if not graph[y][x]:
            a = 0
            dfs(y, x)
            count += 1
            result.append(a)

print(count)
for e in sorted(result):
    print(e, end=' ')