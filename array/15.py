# technique of two-sum
# n1+n2+n3 = 0 
# (n2+n3) = -(n1)
# Sorting
# No duplication check nums[i] == nums[i+1] i++ 
                    # nums[j] == nums[j-1] j--
# Fixed n1 no (duplicate)
# Tc = O(n^2)
# Sc = O(k)

class Solution:
    def threeSum(self, nums):
        n = len(nums)
        if n < 3:
            return []
        
        result = []
        nums.sort()
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            n1 = nums[i]
            target = -n1
            self.twoSum(nums, target, i + 1, n - 1, result)
        
        return result
    
    def twoSum(self, nums, target, i, j, result):
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                result.append([-target, nums[i], nums[j]])
                while i < j and nums[i] == nums[i + 1]:
                    i += 1
                while i < j and nums[j] == nums[j - 1]:
                    j -= 1
                i += 1
                j -= 1


                
