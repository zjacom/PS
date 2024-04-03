template = input()

alpha_flag, num_flag = 0, 0

answer = 1

for i in template:
    if i == "c":
        if not alpha_flag:
            answer *= 26
            alpha_flag, num_flag = 1, 0
        else:
            answer *= 25
            num_flag = 0
    else:
        if not num_flag:
            answer *= 10
            num_flag, alpha_flag = 1, 0
        else:
            answer *= 9
            alpha_flag = 0

print(answer)
        