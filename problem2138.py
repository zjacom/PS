import sys
N = int(input())
s = list(map(int, input()))
e = list(map(int, input()))


def transform(source, target):
    source = source[:]
    count = 0
    for i in range(1, N):
        if source[i - 1] == target[i - 1]:
            continue
        for j in range(i - 1, i + 2):
            if j < N:
                source[j] = 1 - source[j]
        count += 1
    if source == target:
        return count
    return sys.maxsize


a = transform(s, e)


s[0], s[1] = 1 - s[0], 1 - s[1]
b = transform(s, e) + 1

result = min(a, b)
if result == sys.maxsize:
    print(-1)
else:
    print(result)
