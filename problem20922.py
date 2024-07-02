N, K = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0

counter = [0] * (max(arr) + 1)
answer = 0
while right < N:
    if counter[arr[right]] < K:
        counter[arr[right]] += 1
        right += 1
    else:
        counter[arr[left]] -= 1
        left += 1
    answer = max(answer, right - left)

print(answer)