// kadane's algorithm
// Tc = O(n)
// Sc = O(1)

var maxAbsoluteSum = function (nums) {
    let maxSum = 0, minSum = 0, currMax = 0, currMin = 0;
    for(let num of nums){
        currMax = Math.max(num, currMax + num)
        maxSum = Math.max(maxSum, currMax)
        currMin = Math.min(num, currMin + num)
        minSum = Math.min(minSum, currMin)
    }
    return Math.max(maxSum, Math.abs(minSum))
};