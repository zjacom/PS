from collections import deque, defaultdict
import sys
input = sys.stdin.readline

# 설정
queue = deque([(1, 0)])
snake = defaultdict(int)
ladder = defaultdict(int)
visited = [False] * (100 + 1)
result = 0

# 입력
N, M = map(int, input().split())
for _ in range(N):
    s, d = map(int, input().split())
    ladder[s] = d

for _ in range(M):
    s, d = map(int, input().split())
    snake[s] = d

# 로직
def bfs():
    global visited, queue, ladder, snake
    while queue:
        node, cnt = queue.popleft()

        if node == 100:
            print(cnt)
            exit(0)
        
        for i in range(1, 7):
            n = node + i
            if n <= 100 and not visited[n]:
                if ladder[n]:
                    queue.append((ladder[n], cnt + 1))
                    visited[ladder[n]] = True
                elif snake[n]:
                    queue.append((snake[n], cnt + 1))
                    visited[snake[n]] = True
                else:
                    queue.append((n, cnt + 1))
                    visited[n] = True
# 출력
bfs()