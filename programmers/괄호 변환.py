def check(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return True
    
def divide(s):
    a, b = 0, 0
    for i, v in enumerate(s):
        if v == "(":
            a += 1
        else:
            b += 1
        if a == b:
            return s[:i + 1], s[i + 1:]
    
def solution(p):
    if not p:
        return ''
    u, v = divide(p)
    if check(u):
        return u + solution(v)
    else:
        answer = "(" + solution(v) + ")"
        for i in range(1, len(u) - 1):
            if u[i] == ")":
                answer += "("
            else:
                answer += ")"
        return answer