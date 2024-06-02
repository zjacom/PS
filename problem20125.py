N = int(input())

graph = []
for _ in range(N):
    graph.append(input())

for y in range(N):
    for x in range(N):
        if y - 1 >= 0 and graph[y - 1][x] == "*":
            if x - 1 >= 0 and graph[y][x - 1] == "*":
                if y + 1 < N and graph[y + 1][x] == "*":
                    if x + 1 < N and graph[y][x + 1] == "*":
                        hy, hx = y, x
                        break

left, left_size = hx - 1, 0
while True:
    if left < 0 or graph[hy][left] == "_":
        break
    left_size += 1
    left -= 1

right, right_size = hx + 1, 0
while True:
    if right >= N or graph[hy][right] == "_":
        break
    right_size += 1
    right += 1

back, back_size = hy + 1, 0
while True:
    if graph[back][hx] == "_":
        left_leg, right_leg = back + 1, back + 1
        break
    back_size += 1
    back += 1

left_leg_size = 1
while True:
    if left_leg >= N or graph[left_leg][hx - 1] == "_":
        break
    left_leg_size += 1
    left_leg += 1

right_leg_size = 1
while True:
    if right_leg >= N or graph[right_leg][hx + 1] == "_":
        break
    right_leg_size += 1
    right_leg += 1

print(hy + 1, hx + 1)
print(left_size, right_size, back_size, left_leg_size, right_leg_size)