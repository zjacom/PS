# 20922번
from collections import defaultdict

N, K = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
answer = 0
dic = defaultdict(int)

while right < N:
    if dic[arr[right]] == K:
        dic[arr[left]] -= 1
        left += 1
    else:
        dic[arr[right]] += 1
        right += 1
    
    answer = max(answer, right - left)
    
print(answer)