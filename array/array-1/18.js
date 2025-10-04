/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function (nums, target) {
    nums.sort((a, b) => a - b)
    n = nums.length
    const res = []
    if (n < 4) {
        return []
    }
    for (let i = 0; i < n - 3; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue
        }
        for (let j = i + 1; j < n - 2; j++) {
            if (j > i + 1 && nums[j] === nums[j - 1]) {
                continue
            }
            let left = j + 1, right = n - 1
            while (left < right) {
                const total = nums[i] + nums[j] + nums[left] + nums[right]
                if (target === total) {
                    res.push([nums[i], nums[j], nums[right], nums[left]])
                    left++
                    right--
                    while (left < right && nums[left] === nums[left - 1]) {
                        left++
                    }
                    while (left < right && nums[right] === nums[right + 1]) {
                        right--
                    }
                } else if (total < target) {
                    left++
                } else {
                    right--
                }
            }
        }
    }
    return res
};