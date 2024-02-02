import sys
input = sys.stdin.readline

# input
k = int(input())

# logic
result = []
for num in range(2, int(k ** 0.5) + 1):
    while k % num == 0:
        result.append(num)
        k //= num
if k > 1:
    result.append(k)
    
# output
print(1 if len(result) == 0 else len(result))
print(' '.join(map(str, sorted(result))))