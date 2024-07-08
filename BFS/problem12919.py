A = input()
B = input()


def recur(t):
    if not t:
        return
    
    if t == A:
        print(1)
        exit(0)
    
    if t[-1] == "A":
        recur(t[:-1])
    if t[0] == "B":
        recur(t[1:][::-1])

recur(B)
print(0)