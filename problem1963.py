from collections import deque

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

def bfs(start, end):
    global visited
    q = deque([(start, 0)])
    while q:
        node, cnt = q.popleft()

        if node == end:
            return cnt
        
        for n in range(10):
            for i in range(4):
                num = node[:i] + str(n) + node[i + 1:]
                if checker(int(num)) and int(num) > 999:
                    if not visited[int(num)]:
                        q.append((num, cnt + 1))
                        visited[int(num)] = 1
    return "Impossible"

for s, e in arr:
    visited = [0] * 10_000
    visited[int(s)] = 1
    print(bfs(s, e))