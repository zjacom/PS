def transform(time):
    hh, mm = time.split(":")
    return int(hh) * 60 + int(mm)


def solution(book_time):
    book_time = sorted(
        [[transform(start), transform(end) + 10] for start, end in book_time]
    )
    rooms = []
    for start, end in book_time:
        if not rooms:
            rooms.append([end])
            continue
        flag = True
        for i, v in enumerate(rooms):
            if v[-1] <= start:
                flag = False
                rooms[i].append(end)
                break
        if flag:
            rooms.append([end])
    return len(rooms)
