import sys
input = sys.stdin.readline

# input
H, W = map(int, input().split())
arr = list(map(int, input().split()))
max_height = max(arr)
print(max_height)