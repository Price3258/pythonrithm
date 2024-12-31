"""
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 함수를 완성하세요.

prices = [1, 2, 3, 2, 3]
answer = [4, 3, 1, 1, 0]
"""
from collections import deque

def get_price_not_fall_periods(prices):
    result = []
    queue = deque(prices)
    while queue:
        duration = 0
        price = queue.popleft()
        for next_price in queue:
            if price > next_price:
                duration += 1
                break
            duration += 1

        result.append(duration)

    return result


print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 2, 3, 2, 3]))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))
print("정답 = [1, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([10, 9, 9, 3, 5, 10, 2]))
