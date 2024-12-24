# Q.
# 1. 입력으로 소문자의 알파벳 순으로 정렬된 문자열이 입력됩니다.
# 2. 각 알파벳은 중복이 가능합니다.
# 3. 중간에 없는 알파벳이 있을 수도 있습니다.
#
# 입,출력 예시와 같이 입력 문자열에 나타나는 각 알파벳의 종류,갯수를 요약하여 나타내시오.

def summarize_string(input_str):

    length = len(input_str) - 1
    print_array = ""
    count = 1
    for i in range(length):
        if input_str[i] == input_str[i+1]:
            count+=1
        else:
            print_array += f'{input_str[i]}{count}/'
            count=1

    print_array += input_str[length] + str(count)

    return print_array


print(summarize_string("acccdeee"))
print(summarize_string("abbbc"))
print(summarize_string("ahhhhz"))
print(summarize_string("acccdeee"))

# 문제의 번호별 조건에 대한 입력 예시와 출력
# Ex 1)
# abc 	# a1/b1/c1
#
# Ex 2-1)
# aaabbbc	# a3/b3/c1
#
# Ex 2-2)
# abbbc	# a1/b3/c1
#
# Ex 3-1)
# ahhhhz	# a1/h4/z1
#
# Ex 3-2)
# acccdeee	# a1/c3/d1/e3