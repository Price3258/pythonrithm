def solution(phone_book):
    # 해시맵 생성
    phone_hash = {}

    # 전화번호를 해시맵에 저장
    for phone in phone_book:
        phone_hash[phone] = True

    for phone in phone_book:
        prefix = ""
        for char in phone:
            prefix += char
            if prefix in phone_hash and prefix != phone:
                return False

    return True


