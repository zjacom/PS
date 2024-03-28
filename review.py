# 1963번
from collections import deque


def isPrime(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


def bfs(a, b):
    q = deque([(a, 0)])
    visited = [0] * 10000
    visited[a] = 1

    while q:
        node, cnt = q.popleft()
        if node == b:
            return cnt
        node = str(node)

        for i in range(10):
            if int(str(i) + node[1:]) >= 1000 and isPrime(int(str(i) + node[1:])) and not visited[int(str(i) + node[1:])]:
                q.append((int(str(i) + node[1:]), cnt + 1))
                visited[int(str(i) + node[1:])] = 1
            if int(node[0] + str(i) + node[2:]) >= 1000 and isPrime(int(node[0] + str(i) + node[2:])) and not visited[int(node[0] + str(i) + node[2:])]:
                q.append((int(node[0] + str(i) + node[2:]), cnt + 1))
                visited[int(node[0] + str(i) + node[2:])] = 1
            if int(node[:2] + str(i) + node[3]) >= 1000 and isPrime(int(node[:2] + str(i) + node[3])) and not visited[int(node[:2] + str(i) + node[3])]:
                q.append((int(node[:2] + str(i) + node[3]), cnt + 1))
                visited[int(node[:2] + str(i) + node[3])] = 1
            if int(node[:3] + str(i)) >= 1000 and isPrime(int(node[:3] + str(i))) and not visited[int(node[:3] + str(i))]:
                q.append((int(node[:3] + str(i)), cnt + 1))
                visited[int(node[:3] + str(i))] = 1
T = int(input())

answer = []
for _ in range(T):
    a, b = map(int, input().split())
    answer.append((a, b))

for a, b in answer:
    res = bfs(a, b)
    print(res) if res != None else print("Impossible")