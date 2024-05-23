H, W, N, M = map(int, input().split())

count = 0

for y in range(0, H, N + 1):
    for x in range(0, W, M + 1):
        count += 1

print(count)