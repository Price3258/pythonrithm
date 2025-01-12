"""
Q. 음이 아닌 정수들로 이루어진 배열이 있다.
이 수를 적절히 더하거나 빼서 특정한 숫자를 만들려고 한다.
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들기 위해서는 다음 다섯 방법을 쓸 수 있다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target_number이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 반환하시오.

"""

def get_all_ways_by_doing_plus_or_minus(arr, current_index, current_sum, all_ways):
    if current_index == len(arr):
        all_ways.append(current_sum)
        return
    get_all_ways_by_doing_plus_or_minus(arr, current_index + 1, current_sum + arr[current_index],all_ways)
    get_all_ways_by_doing_plus_or_minus(arr, current_index + 1, current_sum - arr[current_index],all_ways)
    return all_ways

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    all_ways = []

    get_all_ways_by_doing_plus_or_minus(array, 0, 0, all_ways)
    target_count = 0

    for way in all_ways:
        if target == way:
            target_count += 1

    return target_count


# 테스트
numbers = [1, 1, 1, 1, 1]
target_number = 3
print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!


def dfs(numbers, target, index, current_sum):
    # 1. 종료 조건: 모든 숫자를 탐색한 경우
    if index == len(numbers):
        # 목표 값을 찾으면 1 반환
        return 1 if current_sum == target else 0

    # 2. 현재 숫자를 더하거나 빼는 두 가지 경우로 분기
    add_case = dfs(numbers, target, index + 1, current_sum + numbers[index])
    subtract_case = dfs(numbers, target, index + 1, current_sum - numbers[index])

    # 3. 두 가지 경우의 결과를 합산하여 반환
    return add_case + subtract_case

def solution(numbers, target):
    return dfs(numbers, target, 0, 0)

# 테스트
numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))  # 출력: 5
