def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


def solution(arrayA, arrayB):
    answer = 0
    # arrayA와 arrayB의 최대공약수
    A, B = arrayA[0], arrayB[0]
    for num in arrayA:
        A = gcd(A, num)
    for num in arrayB:
        B = gcd(B, num)

    flag = True
    for num in arrayB:
        if num % A == 0:
            flag = False
            break
    if flag:
        answer = max(answer, A)
    flag = True
    for num in arrayA:
        if num % B == 0:
            flag = False
            break
    if flag:
        answer = max(answer, B)
    return answer
