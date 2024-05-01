N, M = map(int, input().split())
dic = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    dic[a][b] = True
    dic[b][a] = True

answer = 0
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        for k in range(j + 1, N + 1):
            if dic[i][j] or dic[i][k] or dic[j][k]:
                continue
            answer += 1

print(answer)