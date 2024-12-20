# def find_max_num(array):
#     # 이 부분을 채워보세요!
#     if len(array) !=0:
#         array.sort(reverse=True)
#         return array[0]
#     return 1

def find_max_num(array):
    max_number = array[0]
    for val in array:
        if val > max_number:
            max_number = val
    return max_number




print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))