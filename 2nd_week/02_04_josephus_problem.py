# BOJ 1158
# 요세푸스 문제는 다음과 같다.
#
# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다.
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
# 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
# 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
#
# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

def josephus_problem(n, k): # O(n^2)
    people = list(range(1, n + 1))  # 1부터 N까지의 사람들
    result = []  # 제거된 순서를 저장할 리스트
    index = 0  # 현재 인덱스

    while people:
        # 다음 제거할 사람의 인덱스 계산
        index = (index + k - 1) % len(people)
        result.append(people.pop(index))

    return f"<{', '.join(map(str, result))}>"

# 입력 받기
n, k = map(int, input().split())
print(josephus_problem(n, k))


from collections import deque

def josephus_problem_v2(n, k): # deque 를 사용한 답안 0(n)
    # 1부터 N까지의 사람을 deque로 초기화
    people = deque(range(1, n + 1))
    result = []

    while people:
        # K-1번 회전 (앞의 K-1명을 뒤로 보냄)
        people.rotate(-(k - 1))
        # K번째 사람을 제거하고 결과에 추가
        result.append(people.popleft())

    # 결과 출력 형식 맞추기
    return f"<{', '.join(map(str, result))}>"

# 입력 받기
n, k = map(int, input().split())
print(josephus_problem_v2(n, k))
