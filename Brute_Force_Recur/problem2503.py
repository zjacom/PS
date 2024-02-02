import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# input
hint = []
result = 0
N = int(input())
for _ in range(N):
    hint.append(list(map(int, input().split())))

# logic
def checker(hint_idx, num):
    A, B, C = num // 100, num % 100 // 10, num % 100 % 10
    if A == 0 or B == 0 or C == 0:
        return False
    if A == B or A == C or C == B:
        return False
    Tnum = hint[hint_idx][0]
    TBC, TSC = hint[hint_idx][2], hint[hint_idx][1]

    ball_count, strike_count = 0, 0

    for i, v1 in enumerate(list(str(num))):
        for j, v2 in enumerate(list(str(Tnum))):
            if i == j and v1 == v2:
                strike_count += 1
            elif i != j and v1 == v2:
                ball_count += 1
    
    if ball_count == TBC and strike_count == TSC:
        return True

def recur(hint_idx, num):
    global result
    if num > 987:
        return

    if hint_idx == N:
        result += 1
        recur(0, num + 1)
        return
    
    if checker(hint_idx, num):
        recur(hint_idx + 1, num)
    else:
        recur(0, num + 1)
    
                
# output
recur(0, 123)
print(result)