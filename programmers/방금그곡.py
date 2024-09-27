def convert_time(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)

def change_music(music):
    dic = {'C#' : '1', 'D#' : '2', 'F#' : '3', 'G#' : '4', 'A#' : '5'}
    
    for x, y in dic.items():
        music = music.replace(x, y)
    return music


def solution(m, musicinfos):
    answer = []
    m = change_music(m)
    for musicinfo in musicinfos:
        start, end, title, music = musicinfo.split(',')
        during = convert_time(end) - convert_time(start)
        music = change_music(music)
        if len(music) < during:
            music += music * (during // len(music)) + music[:(during % len(music))]
        elif len(music) > during:
            music = music[:during]

        if m in music:
            answer.append([during, title])
    if not answer:
        return '(None)'
    else:
        return sorted(answer, key=lambda x: (-x[0]))[0][1]