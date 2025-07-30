# Tc = O(n)
# Sc = O(n)

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char_to_index = {}
        word_to_index = {}
        tokens = s.split()
        if len(pattern) != len(tokens):
            return False
        for i in range(len(pattern)):
            char = pattern[i]
            token = tokens[i]
            if char not in char_to_index:
                char_to_index[char] = i
            if token not in word_to_index:
                word_to_index[token] = i
            if char_to_index[char] != word_to_index[token]:
                return False
        return True


# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         char_to_index = {}
#         word_to_index = {}
#         tokens = s.split()
#         if len(pattern) != len(tokens):
#             return False
#         for i in range(len(pattern)):
#             char = pattern[i]
#             token = tokens[i]
#             if char not in char_to_index:
#                 char_to_index[char] = i
#             if token not in word_to_index:
#                 word_to_index[token] = i
#             if char_to_index[char] != word_to_index[token]:
#                 return False
#         return True 