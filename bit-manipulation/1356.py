# Amazon


# Approach-1
# Tc = O(sorting + 1 bit count)
# Tc = O(n.logn + log(num)) [n for loop, logn for sorting, log(num) -> for 1 bit count in any number]
class Solution(object):
    def countOneBit(self, num):
        count = 0
        while num != 0: # log^2(num)
            count += num & 1
            num >>= 1
        return count
    def sortByBits(self, arr): #n.logn
        arr.sort(key = lambda x: (self.countOneBit(x), x))
        return arr
        


# Approach-2(without using lambda function)
# Tc = O(n.logn) [only for sorting and loop]
class Solution(object):
    def sortByBits(self, arr):
        def countOneBit(x):
            return bin(x).count('1')
        arr.sort(key = lambda x: (countOneBit(x), x))
        return arr

