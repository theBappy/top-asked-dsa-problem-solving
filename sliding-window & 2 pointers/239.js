
//  Tc = O(nK) 
//  Sc = O(k)
// brute force 
function bruteForceMaxSlidingWindow(nums, k){
    const result = []
    for(let i = 0 ; i<nums.length; i++){
        result.push(Math.max(...nums.slice(i, i+k)))
    }
    return result
}

//  Tc = O(n) 
//  Sc = O(k)
// Monotonic Deque

function maxSlidingWindow(nums, k) {
    // Initialize a deque (will use array to simulate deque behavior)
    const deq = [];
    const result = [];
    
    for (let i = 0; i < nums.length; i++) {
        // Remove indices from front that are outside current window (i - k + 1 is window start)
        while (deq.length > 0 && deq[0] <= i - k) {
            deq.shift(); // Remove from front
        }
        
        // Remove indices from back whose values are <= current number
        // This maintains deque in decreasing order
        while (deq.length > 0 && nums[deq[deq.length - 1]] <= nums[i]) {
            deq.pop(); // Remove from back
        }
        
        // Add current index to deque
        deq.push(i);
        
        // Once we've processed at least k elements, start recording results
        if (i >= k - 1) {
            // Front of deque always has max for current window
            result.push(nums[deq[0]]); 
        }
    }
    
    return result;
}

// Example usage
const nums = [1, 3, -1, -3, 5, 3, 6, 7];
const k = 3;
console.log(maxSlidingWindow(nums, k)); // Output: [3, 3, 5, 5, 6, 7]
