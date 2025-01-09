def solution(nums):
    max_selectable = len(nums) // 2
    unique_types = len(set(nums))
    return min(max_selectable, unique_types)


"""
폰켓몬
nums는 항상 짝수
"""