N = int(input())
M = int(input())
x = list(map(int, input().split()))
result = max(abs(0 - x[0]), abs(N - x[-1]))

for i in range(M - 1):
    result = max(result, (x[i + 1] - x[i] + 1) // 2)

print(result)