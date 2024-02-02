import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# input
N = int(input())
ingre = [list(map(int, input().split())) for _ in range(N)]
result = sys.maxsize

# logic
def recur(idx, s, ss, use):
    global result, ingre
    if idx == N:
        if use != 0:
            result = min(result, abs(s - ss))
            return
        return

    cs, css = ingre[idx][0], ingre[idx][1]

    recur(idx + 1, s * cs, ss + css, use + 1)
    recur(idx + 1, s, ss, use)

recur(0, 1, 0, 0)
print(result)