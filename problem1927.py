import heapq

N = int(input())
q = []
result = []
for _ in range(N):
    node = int(input())
    if node == 0:
        if not q:
            result.append(0)
        else:
            result.append(heapq.heappop(q))
    else:
        heapq.heappush(q, node)

for res in result:
    print(res)