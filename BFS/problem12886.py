from collections import deque
import sys
input = sys.stdin.readline

# 입력
A, B, C = map(int, input().split())
total = A + B + C
visited = [[False] * (total + 1) for _ in range(total + 1)]
q = deque([(A, B)])
visited[A][B] = True

# 로직
def bfs():
    while q:
        a, b = q.popleft()
        c = total - a - b

        if a == b == c:
            print(1)
            return
        
        for x, y in (a, b), (a, c), (b, c):
            if x < y:
                y -= x
                x += x
            elif x > y:
                x -= y
                y += y
            
            z = total - x - y
            a = min(x, y, z)
            b = max(x, y, z)

            if not visited[a][b]:
                q.append((a, b))
                visited[a][b] = True
    print(0)

# 출력
if total % 3 != 0:
    print(0)
else:
    bfs()