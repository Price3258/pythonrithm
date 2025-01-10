"""
    Q. 연인 코니와 브라운은 광활한 들판에서 ‘나 잡아 봐라’ 게임을 한다.
    이 게임은 브라운이 코니를 잡거나, 코니가 너무 멀리 달아나면 끝난다.
    게임이 끝나는데 걸리는 최소 시간을 구하시오.

    조건은 다음과 같다.
    코니는 처음 위치 C에서 1초 후 1만큼 움직이고,
    이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다.
    즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.

    브라운은 현재 위치 B에서 다음 순간 B – 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
    코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
    브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다
"""
"""
코니는 속도가 1씩 가속하는 등차수열
"""
from collections import deque

from collections import deque

def catch_me(cony_loc, brown_loc):
    max_position = 200000  # 위치 범위
    visited = [[-1] * (max_position + 1) for _ in range(2)]  # 방문 여부와 시간 저장

    # BFS 초기화
    queue = deque([(brown_loc, 0)])  # (현재 위치, 경과 시간)
    visited[0][brown_loc] = 0  # 0초일 때 브라운 위치 방문 기록

    time = 0
    while cony_loc <= max_position:
        # 코니의 위치 계산
        cony_loc += time
        if cony_loc > max_position:  # 코니가 범위를 벗어나면 종료
            break

        # 코니와 브라운의 위치가 같으면 종료
        if visited[time % 2][cony_loc] != -1:
            return time

        # BFS 탐색
        for _ in range(len(queue)):
            current_loc, current_time = queue.popleft()
            for next_loc in (current_loc - 1, current_loc + 1, current_loc * 2):
                if 0 <= next_loc <= max_position and visited[(current_time + 1) % 2][next_loc] == -1:
                    visited[(current_time + 1) % 2][next_loc] = current_time + 1
                    queue.append((next_loc, current_time + 1))

        qwe = {1: 1}
        qwe.keys()
        time += 1  # 시간 증가

    return -1  # 코니를 잡을 수 없을 경우




print("정답 = 5 / 현재 풀이 값 = ", catch_me(11,2))
print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))