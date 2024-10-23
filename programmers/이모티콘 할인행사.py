cases = []

def solution(users, emoticons):
    answer = []
    recur([], len(emoticons))
    for case in cases:
        payments = []
        for discount, price in zip(case, emoticons):
            payments.append((discount, price))
        plus, amount = calc(payments, users)
        answer.append((plus, amount))
    return sorted(answer, key=lambda x: (-x[0], -x[1]))[0]

def recur(temp, length):
    global cases
    if len(temp) == length:
        cases.append(temp[:])
        return
    
    for d in [10, 20, 30, 40]:
        recur(temp + [d], length)

        
def calc(payments, users):
    plus, amount = 0, 0
    for wants, budget in users:
        total = 0
        for discount, price in payments:
            if wants <= discount:
                total += (price * (1 - discount / 100))
        if total >= budget:
            plus += 1
        else:
            amount += total
    return plus, amount