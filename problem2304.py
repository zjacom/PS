N = int(input())

pillars = []
for _ in range(N):
    a, b = map(int, input().split())
    pillars.append((a, b))

pillars = sorted(pillars, key=lambda x: x[0])

maxi = max(pillars, key=lambda x: x[1])
idx = pillars.index(maxi)

lx, lh = pillars[0][0], pillars[0][1]
rx, rh = pillars[N - 1][0], pillars[N - 1][1]
answer = 0

for i in range(1, idx + 1):
    if lh <= pillars[i][1]:
        answer += (pillars[i][0] - lx) * lh
        lx, lh = pillars[i][0], pillars[i][1]

for i in range(N - 2, idx - 1, -1):
    if rh <= pillars[i][1]:
        answer += (rx - pillars[i][0]) * rh
        rx, rh = pillars[i][0], pillars[i][1]

print(answer + maxi[1])