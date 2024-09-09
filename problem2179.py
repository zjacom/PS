import sys

N = int(input())

a = [input() for _ in range(N)]

words = sorted(enumerate(a), key=lambda x: x[1])

dp = [0] * N

def compare(s1, s2):
    if s1 == s2:
        return -sys.maxsize
    
    r = min(len(s1), len(s2))
    count = 0

    for i in range(r):
        if s1[i] == s2[i]:
            count += 1
        else:
            break
    return count

maxi = -1

for i in range(N - 1):
    length = compare(words[i][1], words[i + 1][1])
    if maxi <= length:
        maxi = length
        dp[words[i][0]] = max(dp[words[i][0]], maxi)
        dp[words[i + 1][0]] = max(dp[words[i + 1][0]], maxi)

cnt = 0
for i in range(N):
    if cnt == 0 and dp[i] == maxi:
        print(a[i])
        cnt += 1
        pre = a[i][:maxi]
    elif cnt == 1 and dp[i] == maxi and a[i][:maxi] == pre:
        print(a[i])
        break