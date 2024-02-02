import sys
input = sys.stdin.readline

# input
N = int(input())

# logic
result = []
for num in range(2, int(N ** 0.5) + 1):
    while N % num == 0:
        result.append(num)
        N //= num
if N > 1:
    result.append(N)

# output
for num in sorted(result):
    print(num)