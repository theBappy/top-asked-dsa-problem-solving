// lexicographical next permutation
// Tc = O(n) for finding the pivot + O(n) for finding the successor + O(n) for reversing the suffix + O(1) for swap elements = overall O(n)
// Sc = O(1) in-place,no extra data structure used

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
function nextPermutation(nums) {
    let n = nums.length;
    let pivot = -1;

    // Step 1: Find the pivot (first index where nums[i] > nums[i-1])
    for (let i = n - 1; i > 0; i--) {
        if (nums[i] > nums[i - 1]) {
            pivot = i - 1;
            break;
        }
    }

    // Step 2: Find successor to swap with pivot
    if (pivot !== -1) {
        let successor = n - 1;
        while (successor > pivot && nums[successor] <= nums[pivot]) {
            successor--;
        }
        // Step 3: Swap pivot and successor
        [nums[pivot], nums[successor]] = [nums[successor], nums[pivot]];
    }

    // Step 4: Reverse the suffix (elements after pivot)
    let left = pivot + 1;
    let right = n - 1;
    while (left < right) {
        [nums[left], nums[right]] = [nums[right], nums[left]];
        left++;
        right--;
    }
}

// Test Example
let nums = [1, 2, 3];
nextPermutation(nums);
console.log(nums); // Output: [1, 3, 2]


function nextPermutation(nums){
    let n = nums.length
    let pivot = -1
    for(let i = n-1; i > 0; i--){
        if(nums[i] > nums[i-1]){
            pivot = i - 1
            break
        }
    }
    if(pivot != -1){
        let successor = n-1
        while(successor > pivot && nums[successor] <= nums[pivot]){
            successor--
        }
        [nums[pivot], nums[successor]] = [nums[successor], nums[pivot]]
    }
    let left = pivot + 1
    let right = n - 1
    while(left < right){
        [nums[left], nums[right]] = [nums[right], nums[left]]
        left++
        right--
    }
}



// function nextPermutation(nums){
//     let n = nums.length
//     let pivot = -1
//     for(let i = n-1; i>0;i--){
//         if(nums[i] > nums[i-1]){
//             pivot = i-1
//             break
//         }
//     }
//     if(pivot != -1){
//         let successor = n-1
//         while(successor > pivot && nums[successor] <= nums[pivot]){
//             successor--
//         }
//         [nums[pivot], nums[successor]] = [nums[successor], nums[pivot]]
//     }
//     let left = pivot + 1
//     let right = n-1
//     while(left < right){
//         [nums[left], nums[right]] = [nums[right], nums[left]]
//         left++
//         right--
//     }
// }



// function nextPermutation(nums){
//     let n = nums.length
//     let pivot = -1
//     for(let i = n-1; i>0;i--){
//         if(nums[i] > nums[i-1]){
//             pivot = i-1
//             BroadcastChannel
//         }
//     }
//     if(pivot != -1){
//         let successor = n - 1
//         while(successor > pivot && nums[successor] <= nums[pivot]) {
//             successor--
//         }
//         [nums[pivot], nums[successor]] = [nums[successor], nums[pivot]]
//     }
//     let left = pivot + 1
//     let right = n - 1
//     while(left < right){
//         [nums[left], nums[right]] = [nums[right], nums[left]]
//         left++
//         right--
//     }
// }






