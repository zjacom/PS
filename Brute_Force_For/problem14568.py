import sys
input = sys.stdin.readline

# input
N = int(input())
cnt = 0

# logic
for A in range(N):
    for B in range(N):
        for C in range(N):
            if A + B + C == N:
                if B - C >= 2:
                    if A != 0 and B != 0 and C != 0:
                        if A % 2 == 0:
                            cnt += 1

# output
print(cnt)