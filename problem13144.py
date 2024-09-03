N = int(input())
arr = list(map(int, input().split()))

left, right = 0, 0
result = 0
visited = [False] * 100001

while left <= right and right < N:
    if not visited[arr[right]]:
        visited[arr[right]] = True
        result += right - left + 1
        right += 1
    else:
        while visited[arr[right]]:
            visited[arr[left]] = False
            left += 1

print(result)