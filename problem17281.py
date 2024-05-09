from itertools import permutations

N = int(input())
score_board = []

for _ in range(N):
    score_board.append(list(map(int, input().split())))

lineups = []

for lineup in list(permutations([i for i in range(9)], 9)):
    if lineup[3] != 0:
        continue
    lineups.append(lineup)

answer = 0
while lineups:
    lineup = lineups.pop()
    ining = 0
    score = 0
    idx = 0
    out = 0
    one, two, three = False, False, False
    
    while ining < N:
        action = score_board[ining][lineup[idx % 9]]
        if action == 0:
            out += 1
        elif action == 1:
            # 주자가 없을 때
            if not one and not two and not three:
                one = True
            # 1루
            elif one and not two and not three:
                two = True
            # 12루
            elif one and two and not three:
                three = True
            # 13루
            elif one and not two and three:
                two = True
                three = False
                score += 1
            # 2루
            elif not one and two and not three:
                three = True
                two = False
                one = True
            # 23루
            elif not one and two and three:
                two = False
                score += 1
                one = True
            # 3루
            elif not one and not two and three:
                one = True
                three = False
                score += 1
            # 만루
            elif one and two and three:
                score += 1
        elif action == 2:
            # 주자가 없을 때
            if not one and not two and not three:
                two = True
            # 1루
            elif one and not two and not three:
                one = False
                two = True
                three = True
            # 12루
            elif one and two and not three:
                one = False
                two = True
                three = True
                score += 1
            # 13루
            elif one and not two and three:
                one = False
                two = True
                three = True
                score += 1
            # 2루
            elif not one and two and not three:
                score += 1
            # 23루
            elif not one and two and three:
                three = False
                score += 2
            # 3루
            elif not one and not two and three:
                two = True
                three = False
                score += 1
            # 만루
            elif one and two and three:
                one = False
                two = True
                three = True
                score += 2
        elif action == 3:
            # 주자가 없을 때
            if not one and not two and not three:
                three = True
            # 1루
            elif one and not two and not three:
                one = False
                three = True
                score += 1
            # 12루
            elif one and two and not three:
                one = False
                two = False
                three = True
                score += 2
            # 13루
            elif one and not two and three:
                one = False
                two = False
                score += 2
            # 2루
            elif not one and two and not three:
                two = False
                three = True
                score += 1
            # 23루
            elif not one and two and three:
                two = False
                score += 2
            # 3루
            elif not one and not two and three:
                score += 1
            # 만루
            elif one and two and three:
                one = False
                two = False
                score += 3
        elif action == 4:
            cnt = 1
            if one:
                cnt += 1
            if two:
                cnt += 1
            if three:
                cnt += 1
            score += cnt
            one, two, three = False, False, False
        idx += 1
        if out == 3:
            ining += 1
            out, one, two, three = 0, False, False, False

    answer = max(answer, score)

print(answer)