S = list(''.join(input()))

zero = S.count('0')
one = S.count('1')

zeros = zero // 2
ones = one // 2

temp = []

for i in range(len(S)):
    if S[i] == '0':
        temp.append(S[i])
    else:
        if not ones:
            temp.append(S[i])
        else:
            ones -= 1

temp = temp[::-1]
result = []
for i in range(len(temp)):
    if temp[i] == '1':
        result.append(temp[i])
    else:
        if not zeros:
            result.append(temp[i])
        else:
            zeros -= 1

print(''.join(result[::-1]))