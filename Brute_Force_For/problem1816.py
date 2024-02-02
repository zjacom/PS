import sys
input = sys.stdin.readline

# input
N = int(input())
tc = []
for _ in range(N):
    tc.append(int(input()))

# logic
prime_list = [0, 0]
def check_prime(num):
    global prime_list

    prime_list += [1] * num
    for i in range(2, num + 1):
        if prime_list[i]:
            for j in range(2 * i, num + 1, i):
                prime_list[j] = 0

check_prime(1_000_000)

for c in tc:
    flag = 1
    for i in range(2, min(1_000_001, int(c ** 0.5) + 1)):
        if prime_list[i] and c % i == 0:
            flag = 0
            break
    print("YES" if flag else "NO")
