cases = []

while True:
    s = input().rstrip()

    if s == "end":
        break
    else:
        cases.append(s)

answer = []
for s in cases:
    x_count, o_count = s.count("X"), s.count("O")
    if x_count > o_count + 1:
        answer.append("invalid")
    elif x_count < o_count:
        answer.append("invalid")
    else:
        mate = []
        if s[0] != ".":
            if s[:3].count(s[0]) == 3:
                if s[0] not in mate:
                    mate.append(s[0])
            if s[0] == s[4] and s[0] == s[8]:
                if s[0] not in mate:
                    mate.append(s[0])
            if s[0] == s[3] and s[0] == s[6]:
                if s[0] not in mate:
                    mate.append(s[0])
        if s[1] != ".":
            if s[1] == s[4] and s[1] == s[7]:
                if s[1] not in mate:
                    mate.append(s[1])
        if s[2] != ".":
            if s[2] == s[5] and s[2] == s[8]:
                if s[2] not in mate:
                    mate.append(s[2])
            if s[2] == s[4] and s[2] == s[6]:
                if s[2] not in mate:
                    mate.append(s[2])
        if s[3] != ".":
            if s[3:6].count(s[3]) == 3:
                if s[3] not in mate:
                    mate.append(s[3])
        if s[6] != ".":
            if s[6:9].count(s[6]) == 3:
                if s[6] not in mate:
                    mate.append(s[6])
        if len(mate) > 1:
            answer.append("invalid")
        elif mate == ["X"] and x_count == o_count:
            answer.append("invalid")
        elif "." in s and len(mate) == 0:
            answer.append("invalid")
        elif x_count > o_count and mate == ["O"]:
            answer.append("invalid")
        else:
            answer.append("valid")

for row in answer:
    print(row)