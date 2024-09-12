import sys

N, M, L, K = map(int, input().split())
stars = []
for _ in range(K):
    x, y = map(int, input().split())
    stars.append((x, y))


def calc(x1, y1):
    count = 0
    for x, y in stars:
        if x1 <= x <= x1 + L and y1 <= y <= y1 + L:
            count += 1
    return count


maxi = -sys.maxsize

for i in range(K):
    for j in range(K):        
        sx, sy = min(stars[i][0], stars[j][0]), min(stars[i][1], stars[j][1])

        maxi = max(maxi, calc(sx, sy))

print(K - maxi)