function getMaximumXor(nums, maximumBit) {
    const n = nums.length;
    const result = new Array(n).fill(0);

    // step-1 : Find the total xor
    let XOR = 0;
    for (const num of nums) {
        XOR ^= num;
    }

    // To find flip, first find the mask having all bits set to 1
    const mask = (1 << maximumBit) - 1;

    for (let i = 0; i < n; i++) {
        const k = XOR ^ mask;  // this will give me the flipped value of XOR i.e. my best K
        result[i] = k;

        XOR ^= nums[n - 1 - i];
    }

    return result;
}