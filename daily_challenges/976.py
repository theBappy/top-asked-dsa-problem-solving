def largestPerimeter(nums):
    n = len(nums)
    nums.sort()
    for i in range(n-3, -1, -1):
        if(nums[i] + nums[i+1] > nums[i+2]):
            return nums[i] + nums[i+1] + nums[i+2]
    return 0
