import sys
input = sys.stdin.readline

# input
N = int(input())
tc = list(map(int, input().split()))

# logic
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# output
result = 0
for num in tc:
    if is_prime(num):
        result += 1

print(result)

# 에라토스테네스의 채
prime_list = [0, 0] + ([1] * 1000)
for i in range(2, 1001):
    if prime_list[i]:
        for j in range(i * 2, 1001, i):
            prime_list[j] = 0

cnt = 0
for num in tc:
    if prime_list[num]:
        cnt += 1
print(cnt)