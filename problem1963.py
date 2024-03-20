from collections import deque
import heapq

T = int(input())

arr = []

for _ in range(T):
    a, b = map(str, input().split())
    arr.append((a, b))

def checker(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


def func(start, end):
    global visited
    q = [(0, start)]
    while q:
        cnt, node = heapq.heappop(q)
        if node == end:
            return cnt
        a, b, c, d = node[0], node[1], node[2], node[3]

        for num in range(1, 10):
            num = str(num)
            if num != a and not visited[int(num + b + c + d)]:
                if checker(int(num + b + c + d)):
                    heapq.heappush(q, (cnt + 1, num + b + c + d))
                    visited[int(num + b + c + d)] = 1
        for num in range(10):
            num = str(num)
            if num != b and not visited[int(a + b + num + d)]:
                if checker(int(a + num + c + d)):
                    heapq.heappush(q, (cnt + 1, a + num + c + d))
                    visited[int(a + num + c + d)] = 1
            if num != c and not visited[int(a + b + num + d)]:
                if checker(int(a + b + num + d)):
                    heapq.heappush(q, (cnt + 1, a + b + num + d))
                    visited[int(a + b + num + d)] = 1
        for num in range(1, 10, 2):
            num = str(num)
            if num != d and not visited[int(a + b + c + num)]:
                if checker(int(a + b + c + num)):
                    heapq.heappush(q, (cnt + 1, a + b + c + num))
                    visited[int(a + b + c + num)] = 1


for s, e in arr:
    visited = [0] * 10_000
    visited[int(s)] = 1
    answer = func(s, e)
    print(answer) if answer != None else print("Impossible")