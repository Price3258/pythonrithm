from collections import deque

def is_collect(u):
    stack = []
    for char in u:
        if char == '(':
            stack.append(char)
        elif stack:
            stack.pop()
    return len(stack) == 0

def get_u_v(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""

    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break

    v = ''.join(list(queue))
    return u, v

def convert_revserse(u):
    reversed = ""

    for char in u:
        if char =="(":
            reversed += ")"
        else:
            reversed += "("
    return reversed

def get_answer(p):
    if p == '':  # 1번
        return ''
    u, v = get_u_v(p)  # 2번
    if is_collect(u):  # 3번
        return u + get_answer(v)
    else:  # 4번
        return '(' + get_answer(v) + ')' + convert_revserse(u[1:-1])

def solution(p):
    ## (하고)만 이루어진 문자열 w 가 균형 이라면 ! <-입력 p는 이미 균형임.

    ### p를 균형잡힌 괄호 문자열 -> (와 ) 의 개수가 같아야 함.
    ## p를 u, v로 분리함 v는 빈 문자열 가능
    ### u 가 올바른 괄호 () 면 v를 다시 쪼개서 재귀

    if is_collect(p):
        return p
    else:
        return get_answer(p)