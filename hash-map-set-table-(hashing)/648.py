import collections
from typing import List
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Convert dictionary to a set for O(1) lookups
        roots = set(dictionary)
        
        # Function to find the shortest root for a word
        def find_root(word: str) -> str:
            # Check all possible prefixes from shortest to longest
            for l in range(1, len(word)+1):
                if word[:l] in roots:
                    return word[:l]
            return word
        
        # Process each word in the sentence
        return ' '.join(find_root(word) for word in sentence.split())
# Complexity Analysis:
# Time: O(n*m + k) where:
#   - n = number of words in sentence
#   - m = average word length
# Sc = (K + n.m)

# class Solution:
#     def replaceWords(self, dictionary: List[str], sentence: str) -> str:
#         roots = set(dictionary)
#         def find_root(self, word: str) -> str:
#             for l in range(1, len(word) + 1):
#                 if word[:l] in roots:
#                     return word[:l]
#             return word
#         return ' '.join(find_root(word) for word in sentence.split())
            