"""
Q.
다음과 같이 숫자로 이루어진 배열이 두 개가 있다.
하나는 상품의 가격을 담은 배열이고, 하나는 쿠폰을 담은 배열이다.
쿠폰의 할인율에 따라 상품의 가격을 할인 받을 수 있다.
이 때, 최대한 할인을 많이 받는다면 얼마를 내야 하는가?
단, 할인쿠폰은 한 제품에 한 번씩만 적용 가능하다.

"""

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    total_price = 0

    coupons.sort()
    prices.sort()
    while coupons and prices:
        coupon = coupons.pop()
        price = prices.pop()
        total_price += price - (price * (coupon / 100))

    while prices:
        price = prices.pop()
        total_price += price

    return int(total_price)


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))
print("정답 = 28500 / 현재 풀이 값 = ", get_max_discounted_price([30000], [5]))


def get_max_discounted_price_v2(prices, coupons): ## 강의의 답
    coupons.sort(reverse=True)
    prices.sort(reverse=True)
    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

    while price_index < len(prices) and coupon_index < len(coupons):
        max_discounted_price += prices[price_index] * (100 - coupons[coupon_index]) / 100
        price_index += 1
        coupon_index += 1

    while price_index < len(prices):
        max_discounted_price += prices[price_index]
        price_index += 1

    return max_discounted_price


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price_v2([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price_v2([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price_v2([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price_v2([20000, 100000, 1500000], [10, 10, 10]))

def get_max_discounted_price_v3(prices, coupons):
    # 상품과 쿠폰 정렬 (내림차순으로 정렬하여 가장 비싼 상품에 큰 할인 적용)
    sorted_prices = sorted(prices, reverse=True)
    sorted_coupons = sorted(coupons, reverse=True)

    total_price = 0

    # 쿠폰이 있는 상품에 대해 할인 적용
    for coupon, price in zip(sorted_coupons, sorted_prices): # zip 은 짧은 array의 length 기준으로 for 문이 동작함.
        total_price += price * (1 - coupon / 100)

    # 쿠폰을 다 쓴 뒤 남은 상품의 가격 합산
    total_price += sum(sorted_prices[len(sorted_coupons):])

    return int(total_price)


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price_v3([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price_v3([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price_v3([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price_v3([20000, 100000, 1500000], [10, 10, 10]))