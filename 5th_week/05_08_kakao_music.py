# https://school.programmers.co.kr/learn/courses/30/lessons/17683
import math

"""

C, C#, D, D#, E, F, F#, G, G#, A, A#, B
"""
def convert_sharps(m):
    return m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

def get_play_time(start, end):
    start_h, start_m = start.split(':')
    end_h, end_m = end.split(':')

    return (int(end_h) - int(start_h)) *60 + int(end_m) - int(start_m)

def solution(m, musicinfos):
    answer = None
    music = convert_sharps(m)
    max_play_time = 0

    for info in musicinfos:
        start_time, end_time, name, melody = info.split(",")
        play_time = get_play_time(start_time, end_time)

        melody = convert_sharps(melody)
        melody_repeated_count = math.ceil(play_time / len(melody))
        melody_played = (melody * melody_repeated_count)[:play_time]
        if music in melody_played and play_time > max_play_time:
            answer = name
            max_play_time = play_time

    if not answer:
        return "(None)"
    return answer

m = "ABCDEFG"
music_info = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]

print(solution(m,music_info)) #"HELLO"
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])) #"FOO"
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])) #"WORLD"

