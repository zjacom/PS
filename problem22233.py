N, M = map(int, input().split())

words = []
removed = set()
result = []
for _ in range(N):
    words.append(input())
words.sort()

for _ in range(M):
    context = list(input().split(","))

    for word in context:
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) // 2
            if words[mid] > word:
                right = mid - 1
            elif words[mid] < word:
                left = mid + 1
            else:
                removed.add(word)
                break
    
    result.append(N - len(removed))

for res in result:
    print(res)