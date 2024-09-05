import sys

N = int(input())

words = [input() for _ in range(N)]

words = sorted(enumerate(words), key=lambda x: (x[1], x[0]))

words = [x[1] for x in words]


def compare(s1, s2):
    r = min(len(s1), len(s2))
    count = 0

    for i in range(r):
        if s1[i] == s2[i]:
            count += 1
        else:
            break
    return count

maxi = -1
a, b = 0, 0

for i in range(N - 1):
    length = compare(words[i], words[i + 1])
    if maxi < length and words[i] != words[i + 1]:
        a, b = words[i], words[i + 1]
        maxi = length

print(a, b)