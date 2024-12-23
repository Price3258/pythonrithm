# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때,
# 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오. 만약 그런 문자가 없다면 _ 를 반환하시오.

def find_not_repeating_first_character(string):
    alphabet_occurrence_array = [0] * 26

    for val in string:
        if val.isalpha():
            array_index = ord(val) - ord('a') # 각 알파벳의 인덱스를 구함
            alphabet_occurrence_array[array_index] +=1 # 1씩 더해서 빈도수를 구함

    alphabet_array = []

    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence == 1:
            alphabet_array.append(chr(index + ord("a")))

    for char in string:
        if char in alphabet_array:
            return char

    return "_"
result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))


def find_v2(string):
    # alphabet_occurrence_array = [0] * 26

    for current_index in range(len(string)):
        target_char = string[current_index]  # 현재 인덱스의 문자
        # 현재 문자를 제외하고 동일한 문자가 있는지 확인
        has_duplicate = any(
            i != current_index and string[i] == target_char for i in range(len(string))
        )
        if not has_duplicate:
            return target_char

    return "_"


result = find_v2
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))