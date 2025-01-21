#https://school.programmers.co.kr/learn/courses/30/lessons/17676

def get_start_and_end_time(log_time, duration):
    time = log_time.split(':')
    end_time = (int(time[0]) * 3600 + int(time[1]) * 60 + float(time[2])) * 1000  ## 초로 바꾼후 다시 ms로 변경
    start_time = end_time - duration + 1
    return start_time, end_time


def get_request_count_during_one_second(time, start_and_end_times):
    request_count = 0
    start = time
    end = time + 1000
    for start_and_end_time in start_and_end_times:
        if start_and_end_time[1] >= start and start_and_end_time[0] < end:
            request_count += 1
    return request_count


def solution(lines):
    answer = 0
    start_and_end_times = []
    for info in lines:
        _, time, duration = info.split(' ')
        duration = float(duration.replace('s', '')) * 1000
        start, end = get_start_and_end_time(time, duration)
        start_and_end_times.append([start, end])

    for start_and_end_time in start_and_end_times:
        answer = max(answer, get_request_count_during_one_second(start_and_end_time[0], start_and_end_times),
                     get_request_count_during_one_second(start_and_end_time[1], start_and_end_times))

    return answer


"""
0.1s, 0.312s, 2s 와 같이 최대 소수점 셋째 자리까지 기록하며 뒤에는 초 단위를 의미하는 s로 끝난다.
-> 무조건 ms로 맞춘 후 계산.

2016-09-15 03:10:33.020 0.011s

33.010 ~ 33.020 0.011초 -> ms로 바꾼 후 1ms 더해야함. 
"""