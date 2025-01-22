#https://leetcode.com/problems/group-anagrams/?envType=study-plan-v2&envId=top-interview-150
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        print(result)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            result[sorted_word].append(word)

        return list(result.values())

"""
 풀이 방법 생각한것. 
 아나그램은 정렬하면 다 같은값. 
 정렬한걸 key 값으로 놓고 원래의 word를 list에 넣는 방식으로 품
 마지막에 value 만 리스트로 꺼내옮. 
"""