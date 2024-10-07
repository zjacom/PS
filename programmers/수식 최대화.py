from itertools import permutations

def calc(arr, order):
    for i, v in enumerate(arr):
        if v == order:
            if order == "*":
                arr = calc(arr[:i - 1] + [arr[i - 1] * arr[i + 1]] + arr[i + 2:], order)
                break
            elif order == "-":
                arr = calc(arr[:i - 1] + [arr[i - 1] - arr[i + 1]] + arr[i + 2:], order)
                break
            elif order == "+":
                arr = calc(arr[:i - 1] + [arr[i - 1] + arr[i + 1]] + arr[i + 2:], order)
                break
    return arr
                
    
def solution(expression):
    answer = 0
    arr, prev = [], 0
    for idx, exp in enumerate(expression):
        if not exp.isdigit():
            arr.append(int(expression[prev:idx]))
            arr.append(exp)
            prev = idx + 1
    arr.append(int(expression[prev:len(expression)]))
    
    orders = list(permutations(["+", "*", "-"], 3))
    for order in orders:
        temp = arr[:]
        for o in order:
            print(f'{temp}의 우선순위 연산자는 {o}일 때')
            temp = calc(temp, o)
            print(temp)
        answer = max(answer, abs(temp[0]))
    return answer


print(solution("50*6-3*2"))