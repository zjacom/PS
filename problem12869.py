from itertools import permutations

N = int(input())

SCVs = tuple(map(int, input().split()))

if len(SCVs) == 1:
    SCV = SCVs[0]
    count = 0
    while SCV > 0:
        count += 1
        SCV = SCV - 9
    print(count)
    exit(0)

if len(SCVs) == 2:
    attacks = list(permutations([9, 3], 2))
elif len(SCVs) == 3:
    attacks = list(permutations([9, 3, 1], 3))

dp = [{SCVs}] + [set() for _ in range(999)]

for count in range(1, 1_000):
    for SCV in dp[count - 1]:
        for attack in attacks:
            flag, t = True, []
            for ele in zip(SCV, attack):
                if ele[0] - ele[1] > 0:
                    flag = False
                t.append(ele[0] - ele[1])
            if flag:
                print(count)
                exit(0)
            dp[count].add(tuple(t))

