#https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150

## two pointer

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = ''.join(re.findall(r'[a-zA-Z0-9]', s.lower()))

        mid = len(alphabet) // 2
        head = 0
        tail = len(alphabet) - 1

        if len(alphabet) == 1:
            return True

        for i in range(mid):
            if alphabet[head] == alphabet[tail]:
                head += 1
                tail += -1
                continue
            else:
                return False

        return True

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))