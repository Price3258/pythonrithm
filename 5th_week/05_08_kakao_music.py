# https://school.programmers.co.kr/learn/courses/30/lessons/17683


"""

C, C#, D, D#, E, F, F#, G, G#, A, A#, B
"""
def convert_sharps(m):
    return m.replace("C#","c").replace("D#","d").replace("G#","g").replace("A#","a")

def solution(m, musicinfos):
    answer = ''

    m = convert_sharps(m)

    print(m)



    return '(None)'

m = "ABCDEFG"
music_info = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]

print(solution(m,music_info)) #"HELLO"
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])) #"FOO"
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])) #"WORLD"

