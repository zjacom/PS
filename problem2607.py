N = int(input())
words = [input().strip() for _ in range(N)]
first_word = words[0]
count = 0

for i in range(1, N):
    if len(first_word) <= len(words[i]):
        temp = list(''.join(words[i]))
        for word in first_word:
            if word in temp:
                temp.remove(word)
        if len(temp) <= 1:
            count += 1
    else:
        temp = list(''.join(first_word))
        for word in words[i]:
            if word in temp:
                temp.remove(word)
        if len(temp) == 1:
            count += 1

print(count)