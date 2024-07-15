# 12919번

S = input()
T = input()


def recur(s):
    if s == S:
        print(1)
        exit(0)
    if len(s) < len(S):
        return
    
    if s[-1] == "A":
        recur(s[:-1])
    
    if s[0] == "B":
        recur(s[1:][::-1])


recur(T)
print(0)
