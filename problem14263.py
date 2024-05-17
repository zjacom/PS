from collections import defaultdict
import heapq

N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]

# 카드의 크기 정보를 담을 딕셔너리
cards = {}

# 카드의 왼쪽, 오른쪽, 위, 아래를 구하는 로직
for y in range(N):
    for x in range(M):
        if grid[y][x] != ".":
            if grid[y][x] not in cards:
                cards[grid[y][x]] = [x, x, y, y] # left, right, up, down
            else:
                cards[grid[y][x]][0] = min(cards[grid[y][x]][0], x)
                cards[grid[y][x]][1] = max(cards[grid[y][x]][1], x)
                cards[grid[y][x]][2] = min(cards[grid[y][x]][2], y)
                cards[grid[y][x]][3] = max(cards[grid[y][x]][3], y)


# 위상 정렬을 위한 딕셔너리
indegrees = {card: 0 for card in cards}
graph = defaultdict(list)


for card, (left, right, up, down) in cards.items():
    for y in range(up, down + 1):
        for x in range(left, right + 1):
            if grid[y][x] == ".":
                print(-1)
                exit(0)
            if grid[y][x] != card and grid[y][x] not in graph[card]:
                graph[card].append(grid[y][x])
                indegrees[grid[y][x]] += 1

order = []
q = []
for card in indegrees:
    if indegrees[card] == 0:
        heapq.heappush(q, card)

while q:
    node = heapq.heappop(q)
    order.append(node)

    for nxt in graph[node]:
        indegrees[nxt] -= 1
        if indegrees[nxt] == 0:
            heapq.heappush(q, nxt)

if len(order) != len(cards):
    print(-1)
else:
    print(''.join(order))