# Google, Apple, Facebook
# Longest Prefix 
# Any numbers length, number of digits => (log(base 10)Number + 1)

import math
class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        st = set()
        for val in arr1:
            while val not in st and val > 0:
                st.add(val)
                val //= 10
        result = 0
        for num in arr2:
            while num not in st and num > 0:
                num //= 10
            if num > 0:
                result = max(result, int(math.log10(num) + 1))
        return result


# Trie Approach
# T.C : O(m⋅d+n⋅d)
# S.C : O(m⋅d)
class TrieNode:
    def __init__(self):
        self.children = [None] * 10

class Solution:
    def getTrieNode(self):
        return TrieNode()
    
    def insert(self, num, root):
        crawl = root
        numStr = str(num)
        for ch in numStr:
            idx = int(ch)
            if crawl.children[idx] is None:
                crawl.children[idx] = self.getTrieNode()
            crawl = crawl.children[idx]

    def search(self, num, root):
        crawl = root
        numStr = str(num)
        length = 0
        for ch in numStr:
            idx = int(ch)
            if crawl.children[idx] is not None:
                length += 1
                crawl = crawl.children[idx]
            else:
                break
        return length


    def longestCommonPrefix(self, arr1, arr2):
        root = self.getTrieNode()

        for num in arr1:
            self.insert(num, root)

        result = 0
        for num in arr2:
            result = max(result, self.search(num, root))

        return result
