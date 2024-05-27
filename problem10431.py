P = int(input())

results = []
for k in range(1, P + 1):
    arr = list(map(int, input().split()))[1:]
    count = 0
    for i in range(19):
        for j in range(i + 1, 20):
            if arr[i] > arr[j]:
                count += 1
                arr[i], arr[j] = arr[j], arr[i]
    results.append((k, count))

for res in results:
    print(*res)
