N, K = map(int, input().split())
arr = list(''.join(input()))
visited = [False] * N
count = 0
for i in range(N):
    if arr[i] == "P":
        left, right = i - K, i + K + 1
        if left < 0:
            left = 0
        if right > N:
            right = N

        for j in range(left, right):
            if arr[j] == "H" and not visited[j]:
                count += 1
                visited[j] = True
                break

print(count)