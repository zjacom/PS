from collections import deque, defaultdict
import sys
input = sys.stdin.readline

# input
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dy, dx = [1, 0, 0, -1], [0, -1, 1, 0]
start_y, start_x = 0, 0 # 상어가 있는 위치!
fish = defaultdict(int) # 크기별로 있는 물고기의 수
for y in range(N):
    for x in range(N):
        if 0 < arr[y][x] <= 6:
            fish[arr[y][x]] += 1
        if arr[y][x] == 9:
            start_y, start_x = y, x 

# logic
def bfs(y, x, size, cnt, exp):
    q = deque([(y, x, size, cnt, exp)])
    while q:
        cy, cx, csize, ccnt, cexp = q.popleft()
        # 남은 물고기 수와 더 레벨업 할 수 없다면 ccnt 리턴
        # temp = 0
        # for s in range(1, csize):
        #     temp += fish[s]
        
        # if temp == 0:
        #     return ccnt

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] < csize:
                    if arr[ny][nx] == 0:
                        q.append((ny, nx, size, ccnt + 1, cexp))
                    else:
                        fish[arr[ny][nx]] -= 1
                        cexp += 1
                        if cexp == csize:
                            q.append((ny, nx, size + 1, ccnt + 1, 0))
                            arr[ny][nx] = 0
                        else:
                            q.append((ny, nx, size, ccnt + 1, cexp))
                            arr[ny][nx] = 0
                elif arr[ny][nx] == csize:
                    q.append((ny, nx, size, ccnt + 1, cexp))

    
# output
arr[start_y][start_x] = 0
print(bfs(start_y, start_x, 2, 0, 0))