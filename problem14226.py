import sys
input = sys.stdin.readline
from collections import deque

# input
S = int(input())

q = deque([1])
visited = [[False] * 10_000 for _ in range(10_000)]
time = -1
clip = 0
visited[1][0] = True
while q:
    time += 1
    for _ in range(len(q)):
        cd = q.popleft()
        if cd == S:
            print(time)
            exit(0)
        # clip -> 이모티콘
        if clip != 0 and not visited[cd + clip][clip]:
            q.append(cd + clip)
        # 화면 - 1
        if cd != 0 and not visited[cd - 1][clip]:
            q.append(cd - 1)
        # 이모티콘 -> clip
        if not visited[cd][cd]:
            q.append(cd)
            visited[cd][cd] = True
            clip = cd