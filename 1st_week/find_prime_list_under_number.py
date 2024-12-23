# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
#
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
#  ```python
# # 20이 입력된다면, 아래와 같이 반환해야 합니다!
# [2, 3, 5, 7, 11, 13, 17, 19]
# ```
def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!

    prime_numbers = []

    for val in range(1, number+1):
        count =0
        for idx in range(1, val+1):
            if val % idx == 0:
                count +=1
        if count ==2:
            prime_numbers.append(val)

    return prime_numbers


result = find_prime_list_under_number(20)

print(result)
print(find_prime_list_under_number(34))
