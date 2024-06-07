N = int(input())
status = [2] + list(map(int, input().split()))
S = int(input())

for _ in range(S):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(1, 101):
            if num * i <= N:
                status[num * i] ^= 1
            else:
                break
    else:
        status[num] ^= 1
        if num - 1 > 0 and num < N:
            left, right = num - 1, num + 1
            while True:
                if left < 1 or right > N:
                    break
                if status[left] != status[right]:
                    break
                status[left] ^= 1
                status[right] ^= 1
                left -= 1
                right += 1


for i in range(1, N + 1, 20):
    print(*status[i:i+20])