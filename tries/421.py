# Microsoft
# Bit Trie(XOR) -> left for 0 and right for 1
# Bit Trie max height -> log(num)
# Iterating bit trie -> n * log(max no) 
# Tc = n * log(max no) [32 bit integer, so max height 32 too] => Tc = n * log(32) => O(n*32) => O(n)
# Sc is like Tc also
class TrieNode:
    def __init__(self):
        self.left = None
        self.right = None
    

class Solution: 
    def insert(self, root, num):
        pCrawl = root
        for i in range(31, -1, -1):
            ith_bit = (num >> i) & 1
            if ith_bit == 0:
                if pCrawl.left is None:
                    pCrawl.left = TrieNode()
                pCrawl = pCrawl.left
            else:
                if pCrawl.right is None:
                    pCrawl.right = TrieNode()
                pCrawl = pCrawl.right
    
    def findMaxXor(self, root, num):
        maxXor = 0
        pCrawl = root
        for i in range(31, -1, -1):
            ith_ibt = (num >> i) & 1
            if ith_ibt == 1:
                if pCrawl.left is not None:
                    maxXor += (1 << i)
                    pCrawl = pCrawl.left
                else: 
                    pCrawl = pCrawl.right
            else:
                if pCrawl.right is not None:
                    max += (1 << i)
                    pCrawl = pCrawl.right
                else:
                    pCrawl = pCrawl.left
        return maxXor

    def findMaximumXor(self, nums):
        root = TrieNode()
        for num in nums:
            self.insert(root, num)
        maxResult = 0
        for num in nums:
            temp = self.findMaxXor(root, num)
            maxResult = max(maxResult, temp)
        return maxResult