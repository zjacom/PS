import sys
from collections import deque


def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))
    return answer

def bfs(place):
    case = []
    for y in range(5):
        for x in range(5):
            if place[y][x] == "P":
                case.append((y, x))
    
    for y, x in case:
        visited = [[sys.maxsize] * 5 for _ in range(5)]
        q = deque([(y, x)])
        visited[y][x] = 0

        while q:
            cy, cx = q.popleft()
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < 5 and 0 <= nx < 5:
                    if place[ny][nx] != "X":
                        if visited[ny][nx] > visited[cy][cx] + 1:
                            if place[ny][nx] == "P" and visited[cy][cx] <= 1:
                                return 0
                            q.append((ny, nx))
                            visited[ny][nx] = visited[cy][cx] + 1
    return 1