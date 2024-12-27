"""
Q. 배달의 민족 서버 개발자로 입사했다.
상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때, 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.
그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.
"""

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):

    menus.sort()
    orders.sort()

    # current_index = len(menus) // 2

    value =[]

    for i in range(len(menus)):
        for j in range(len(orders)):
            if orders[j] == menus[i]:
                value.append(orders[j])

    return len(value) == len(orders)


result = is_available_to_order(shop_menus, shop_orders)
print(result)