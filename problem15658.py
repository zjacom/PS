import sys

N = int(input())
arr = list(map(int, input().split()))
a, s, m, d = map(int, input().split())
mini, maxi = sys.maxsize, -sys.maxsize

def recur(idx, total, a, s, m, d):
    global mini, maxi
    if idx == N:
        mini = min(mini, total)
        maxi = max(maxi, total)
        return
    if a > 0:
        recur(idx + 1, total + arr[idx], a - 1, s, m, d)
    if s > 0:
        recur(idx + 1, total - arr[idx], a, s - 1, m, d)
    if m > 0:
        recur(idx + 1, total * arr[idx], a, s, m - 1, d)
    if d > 0:
        if total < 0:
            total = -total
            recur(idx + 1, -(total // arr[idx]), a, s, m, d - 1)
        else:
            recur(idx + 1, total // arr[idx], a, s, m, d - 1)

recur(1, arr[0], a, s, m, d)

print(maxi)
print(mini)