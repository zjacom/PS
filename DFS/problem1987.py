import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# DFS 함수 정의
def dfs(x, y, count):
    global result
    # 현재 위치의 알파벳을 visited 리스트에 추가
    visited[ord(board[x][y]) - ord('A')] = True
    result = max(result, count)

    # 네 방향으로 이동하면서 조건을 만족하면 재귀 호출
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not visited[ord(board[nx][ny]) - ord('A')]:
            dfs(nx, ny, count + 1)
    
    # 재귀 호출이 끝난 후, 현재 위치의 알파벳을 visited 리스트에서 제거
    visited[ord(board[x][y]) - ord('A')] = False

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
visited = [False] * 26  # 알파벳의 개수(26개)만큼 visited 배열 생성
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우 방향

result = 0
dfs(0, 0, 1)  # (0, 0)에서 시작하여 최소 1칸을 지날 수 있으므로 초기 count를 1로 설정
print(result)
