// Tc = O(n)
// Sc = O(n)
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let map = new Map()
    for (let i = 0;i<nums.length; i++){
        let complement = target - nums[i]
        if(map.has(complement)){
            return [map.get(complement),i]
        }
        map.set(nums[i],i)
    }
    return []
};

var twoSum = function(nums, target){
    let list = {}
    for(let i = 0; i<nums.length; i++){
        let diff = target - nums[i]
        if(list.hasOwnProperty(diff)){
            return [list[diff], i]
        }
        list[nums[i]] = i
    }
}