# 14658번

n, m, l, k = map(int, input().split())

stars = []

for _ in range(k):
    x, y = map(int, input().split())
    stars.append((x, y))

def counting_stars(x1, y1):
    count = 0
    for x, y in stars:
        if x1 <= x <= x1 + l and y1 <= y <= y1 + l:
            count += 1
    
    return count


maxi = 0
for i in range(k):
    for j in range(k):
        x1, y1 = min(stars[i][0], stars[j][0]), min(stars[i][1], stars[j][1])
        maxi = max(maxi, counting_stars(x1, y1))


print(k - maxi)