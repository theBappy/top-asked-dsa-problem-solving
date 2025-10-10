from typing import List
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def are_anagrams(s1: str, s2: str) -> bool:
            count = [0] * 26
            for x in s1:
                count[ord(x) - ord('a')] += 1
            for x in s2:
                count[ord(x) - ord('a')] -= 1
            for val in count:
                if val != 0:
                    return False
            return True
        i = 1
        while i < len(words):
            if are_anagrams(words[i-1], words[i]):
                del words[i]
            else:
                i += 1
        return words