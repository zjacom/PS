import sys
input = sys.stdin.readline

# input
n = int(input())

# logic
result = 0

for i in range(2, (n // 2) + 1):
    result += ((n // i) - 1) * i

# output
print(result % 1_000_000)
