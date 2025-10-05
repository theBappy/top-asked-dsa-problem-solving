
var nextPermutation = function (nums) {
    const n = nums.length
    let swap_index = -1
    for (let i = n - 1; i > 0; i--) {
        if (nums[i] > nums[i - 1]) {
            swap_index = i - 1
            break
        }
    }
    if (swap_index !== -1) {
        let just_greater = swap_index
        for (let j = n - 1; j > swap_index; j--) {
            if (nums[j] > nums[swap_index]) {
                just_greater = j
                break
            }
        }
        [nums[swap_index], nums[just_greater]] = [nums[just_greater], nums[swap_index]]
    }
    let left = swap_index + 1, right = n - 1;
    while (left < right) {
        [nums[left], nums[right]] = [nums[right], nums[left]]
        left++
        right--
    }
};