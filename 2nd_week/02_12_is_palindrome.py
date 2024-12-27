

def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n - i - 1]:
            return False
    return True

input = "abcba"

print(is_palindrome(input))


def is_palindrome_v2(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])

input = "abcba"

print(is_palindrome_v2(input))

from collections import deque

def is_palindrome_deque(string):
   dq = deque(string)

   while dq:
       if dq.popleft() != dq.pop():
           return False

       return True


input = "abcba"

print(is_palindrome_deque(input))