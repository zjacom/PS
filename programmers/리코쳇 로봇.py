import sys
from collections import deque

def solution(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == "G":
                ty, tx = y, x
                break
    
    answer = bfs(board)[ty][tx]
    if answer == sys.maxsize:
        return -1
    return answer

def bfs(board):
    dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
    visited = [[sys.maxsize] * len(board[0]) for _ in range(len(board))]
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == "R":
                sy, sx = y, x
                break
    visited[sy][sx] = 0
    
    q = deque([(sy, sx)])
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < len(board) and 0 <= nx < len(board[0]):
                if board[ny][nx] == "." or board[ny][nx] == "G":
                    ny, nx = move(board, y, x, dy[i], dx[i])
                    if visited[ny][nx] > visited[y][x] + 1:
                        q.append((ny, nx))
                        visited[ny][nx] = visited[y][x] + 1
                else:
                    continue
    return visited

def move(board, y, x, dy, dx):
    cy, cx = y, x
    while True:
        cy = cy + dy
        cx = cx + dx
        if cy >= len(board) or cx >= len(board[0]) or cy < 0 or cx < 0:
            return (cy - dy, cx - dx)
        elif board[cy][cx] == "D":
            return (cy - dy, cx - dx)
        elif board[cy][cx] == ".":
            continue
