N = int(input())

pillars = []
for _ in range(N):
    a, b = map(int, input().split())
    pillars.append((a, b))

pillars = sorted(pillars, key=lambda x: x[0])

left, right = 0, N - 1
lx, lh = pillars[left][0], pillars[left][1]
rx, rh = pillars[right][0], pillars[right][1]
answer = 0
while left < right:
    if lh < rh:
        left += 1
        if pillars[left][1] > lh:
            answer += (pillars[left][0] - lx) * pillars[left][1]
            lx, lh = pillars[left][0], pillars[left][1]
    elif rh < lh:
        right -= 1
        if pillars[right][1] > rh:
            answer += (rx - pillars[right][0]) * pillars[right][1]
            rx, rh = pillars[right][0], pillars[right][1]
    else:
        left += 1
        right -= 1

print(answer)