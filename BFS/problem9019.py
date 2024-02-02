from collections import deque
import sys
input = sys.stdin.readline

# 입력
T = int(input())

# 로직
def func_d(n):
    return int(n * 2 % 10000)


def func_s(n):
    if n == 0:
        return 9999
    else:
        return n - 1


def func_l(n):
    d1, e1 = n // 1000, n % 1000
    d2, e2 = e1 // 100, e1 % 100
    d3, d4 = e2 // 10, e2 % 10

    return int((d2 * 1000) + (d3 * 100) + (d4 * 10) + d1)


def func_r(n):
    d1, e1 = n // 1000, n % 1000
    d2, e2 = e1 // 100, e1 % 100
    d3, d4 = e2 // 10, e2 % 10

    return int((d4 * 1000) + (d1 * 100) + (d2 * 10) + d3)


def bfs(src, dst):
    q = deque([(src, "")])
    visited = [False] * 10000
    visited[src] = True
    while q:
        s, p = q.popleft()
        if s == dst:
            return p
        nd, ns, nl, nr = func_d(s), func_s(s), func_l(s), func_r(s)
        if 0 <= nd < 10000 and not visited[nd]:
            q.append((nd, p + "D"))
            visited[nd] = True
        if 0 <= ns < 10000 and not visited[ns]:
            q.append((ns, p + "S"))
            visited[ns] = True
        if 0 <= nl < 10000 and not visited[nl]:
            q.append((nl, p + "L"))
            visited[nl] = True
        if 0 <= nr < 10000 and not visited[nr]:
            q.append((nr, p + "R"))
            visited[nr] = True

# 출력
result = []
for _ in range(T):
    s, d = map(int, input().split())
    result.append(bfs(s, d))

for r in result:
    print(r)