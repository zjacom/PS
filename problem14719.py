H, W = map(int, input().split())
blocks = list(map(int, input().split()))

max_index, max_height = 0, 0

for i, h in enumerate(blocks):
    if max_height < h:
        max_index, max_height = i, h
answer = 0
left, right = 0, 0
while left < max_index:
    if blocks[right] < blocks[left]:
        answer += blocks[left] - blocks[right]
        left += 1
    else:
        right += 1

print(answer)