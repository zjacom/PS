N, K = map(int, input().split())
belt = list(map(int, input().split()))
robots = [] # [N, N + 1, N + 2 ... ]
step = 0

while True:
    step += 1

    for i in range(len(robots)):
        robots[i] += 1
        if robots[i] == N:
            robots.pop(0)
    
    belt = [belt[-1]] + belt[:-1]

    for i in range(len(robots)):
        if robots[i] + 1 not in robots[:i] and belt[robots[i] + 1] > 0:
            belt[robots[i] + 1] -= 1
            robots[i] += 1
    
    if belt[0] > 0:
        belt[0] -= 1
        robots.append(0)

    if belt.count(0) >= K:
        break

print(step)