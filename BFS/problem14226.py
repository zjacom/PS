import sys
input = sys.stdin.readline
from collections import deque

# input
S = int(input())

q = deque([(1, 0)])
visited = [[0] * (5_001) for _ in range(5_001)]

while q:
    cd, clip = q.popleft()
    if cd == S:
        print(visited[cd][clip])
        break
    
    # 이모티콘 -> clip
    if cd < S and not visited[cd][cd]:
        q.append((cd, cd))
        visited[cd][cd] = visited[cd][clip] + 1
    # clip -> 이모티콘
    if clip != 0 and cd + clip <= S and not visited[cd + clip][clip]:
        q.append((cd + clip, clip))
        visited[cd + clip][clip] = visited[cd][clip] + 1
    # 화면 - 1
    if 0 < cd and not visited[cd - 1][clip]:
        q.append((cd - 1, clip))
        visited[cd - 1][clip] = visited[cd][clip] + 1

