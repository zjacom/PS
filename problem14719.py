H, W = map(int, input().split())
blocks = list(map(int, input().split()))
answer = 0
for i in range(1, W - 1):
    left = max(blocks[:i])
    right = max(blocks[i:])

    height = min(left, right)

    if height > blocks[i]:
        answer += height - blocks[i]

print(answer)