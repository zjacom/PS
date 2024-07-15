import re


def recur(arr, result, idx):
    global answer
    if len(result) == 2 * N - 1:
        if eval(re.sub(r'\s+', '', result)) == 0:
            answer.append(result)

    if idx < N:
        recur(arr, result + "+" + arr[idx], idx + 1)
        recur(arr, result + "-" + arr[idx], idx + 1)
        recur(arr, result + " " + arr[idx], idx + 1)
    

total = []
for _ in range(int(input())):
    N = int(input())
    answer = []
    recur([str(n) for n in range(1, N + 1)], "1", 1)

    for ans in sorted(answer):
        total.append(ans)
    total.append("")

for t in total[:-1]:
    print(t)
