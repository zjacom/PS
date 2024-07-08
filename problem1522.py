import sys

answer = sys.maxsize
s = input()
count = s.count("a")
if count == 0:
    print(0)
    exit(0)

for i in range(len(s)):
    if i + count < len(s):
        answer = min(answer, s[i:i + count].count("b"))
    else:
        answer = min(answer, (s[i:] + s[:(i + count) % len(s)]).count("b"))

print(answer)