N = int(input())
arr = list(map(int, input().split()))

answer = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == arr[i]:
            if answer[j]:
                continue
            answer[j] = i + 1
            break
        if answer[j] == 0:
            cnt += 1

print(*answer)