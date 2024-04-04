N, M = map(int, input().split())

graph = [list(input().strip()) for _ in range(N)]

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
visited = [[0] * M for _ in range(N)]
answer = []
count = 0

for y in range(N):
    for x in range(M):
        if graph[y][x] == "*":
            for i in range(1, 51):
                cnt = 0
                for l in range(1, i + 1):
                    for j in range(4):
                        ny, nx = y + (dy[j] * l), x + (dx[j] * l)
                        if ny < 0 or ny >= N or nx < 0 or nx >= M:
                            break
                        if graph[ny][nx] == "*":
                            cnt += 1
                if cnt == 4 * i:
                    count += 1
                    visited[y][x] = 1
                    for l in range(1, i + 1):
                        for k in range(4):
                            ny, nx = y + (dy[k] * l), x + (dx[k] * l)
                            visited[ny][nx] = 1
                    answer.append((y + 1, x + 1, i))

for y in range(N):
    for x in range(M):
        if graph[y][x] == "*" and not visited[y][x]:
            print(-1)
            exit(0)

print(count)
for row in answer:
    print(*row)