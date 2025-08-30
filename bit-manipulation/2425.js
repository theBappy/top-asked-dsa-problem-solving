

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var xorAllNums = function(nums1, nums2) {
    const m = nums1.length
    const n = nums2.length
    const mp = new Map()
    for(const num of nums1){
        mp.set(num, (mp.get(num) || 0) + n)
    }
    for(const num of nums2){
        mp.set(num, (mp.get(num) || 0) + m)
    }
    let result = 0
    for(const [num, freq] of mp.entries()){
        if(freq % 2 !== 0){
            result ^= num
        }
    }
    return result
};



/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var xorAllNums = function(nums1, nums2) {
    const m = nums1.length
    const n = nums2.length
    let XOR = 0
    if(m % 2 !== 0){
        for(const num of nums2){
            XOR ^= num
        }
    }
    if(n % 2 !== 0){
        for(const num of nums1){
            XOR ^= num
        }
    }
    return XOR
};