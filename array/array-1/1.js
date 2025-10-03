function twoSum(nums, target) {
    const mp = new Map();
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        const remaining = target - num;
        if (mp.has(remaining)) {
            return [mp.get(remaining), i];
        }
        mp.set(num, i);
    }
    return [];
}