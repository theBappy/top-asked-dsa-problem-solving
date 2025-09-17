from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums):
        result = []
        for num in nums:
            while result:
                prev = result[-1]
                curr = num
                GCD = gcd(prev, curr)
                if GCD == 1:
                    break
                result.pop()
                LCM = prev // GCD * curr
                num = LCM
            result.append(num)
        return num

# from math import gcd
# class Solution:
#     def replaceNonCoprimes(self, nums):
#         result = []
#         for num in nums:
#             while result:
#                 prev = result[-1]
#                 curr = num
#                 GCD = gcd(prev, num)
#                 if GCD == 1:
#                     break
#                 result.pop()
#                 LCM = prev // GCD * curr
#                 num = LCM
#             result.append(num)
#         return num