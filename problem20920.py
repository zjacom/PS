from collections import Counter
import heapq
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

words = []
for _ in range(N):
    word = input().strip()
    if len(word) >= M:
        words.append(word)

counter = Counter(words)

q = []
for key, value in counter.items():
    heapq.heappush(q, (-value, -len(key), key))

while q:
    word = heapq.heappop(q)[2]
    print(word)
