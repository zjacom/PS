import heapq
# N = int(input())

# arr = list(map(int, input().split()))

# for _ in range(N - 1):
#     for num in list(map(int, input().split())):
#         arr.append(num)
#     arr.sort()
#     arr = arr[N:2 * N]

# print(min(arr))

q = []
for num in list(map(int, input().split())):
    heapq.heappush(q, num)

for _ in range(N - 1):
    for num in list(map(int, input().split())):
        if num > q[0]:
            heapq.heappop(q)
            heapq.heappush(q, num)

print(q[0])