import sys
sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
maxi = -sys.maxsize

