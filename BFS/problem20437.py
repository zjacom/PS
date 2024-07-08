import sys

T = int(input())

case = []
for _ in range(T):
    s = input()
    k = int(input())
    case.append((s, k))

for s, k in case:
    mini, maxi = sys.maxsize, -sys.maxsize
    for i in range(len(s) - 1):
        prefix, cnt = s[i], 1
        for j in range(i + 1, len(s)):
            if prefix == s[j]:
                cnt += 1
                if cnt == k:
                    mini = min(mini, j - i + 1)
                    maxi = max(maxi, j - i + 1)
                    break
    if mini == sys.maxsize:
        print(-1)
    else:
        print(mini, maxi)