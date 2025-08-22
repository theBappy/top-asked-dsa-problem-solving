
function makeArrayIncreasing(arr1, arr2) {
    // Sort and deduplicate arr2 for efficient binary search
    const sortedArr2 = [...new Set(arr2)].sort((a, b) => a - b);
    const memo = new Map();
    function solve(idx, prev) {
        if (idx === arr1.length) {
            return 0;
        }
        
        const memoKey = `${idx},${prev}`;
        if (memo.has(memoKey)) {
            return memo.get(memoKey);
        }
        
        let result1 = Infinity;
        
        // Option 1: Keep current element if it's greater than previous
        if (arr1[idx] > prev) {
            result1 = solve(idx + 1, arr1[idx]);
        }
        
        let result2 = Infinity;
        
        // Option 2: Replace current element with next greater element from arr2
        const nextGreaterIndex = upperBound(sortedArr2, prev);
        
        if (nextGreaterIndex < sortedArr2.length) {
            result2 = 1 + solve(idx + 1, sortedArr2[nextGreaterIndex]);
        }
        
        const result = Math.min(result1, result2);
        memo.set(memoKey, result);
        return result;
    }
    
    function upperBound(arr, target) {
        let left = 0;
        let right = arr.length;
        
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (arr[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        return left;
    }
    
    const result = solve(0, -Infinity);
    return result === Infinity ? -1 : result;
}

// Test cases
console.log("Test Case 1:");
console.log("arr1 = [1, 5, 3, 6, 7], arr2 = [1, 3, 2, 4]");
console.log("Result:", makeArrayIncreasing([1, 5, 3, 6, 7], [1, 3, 2, 4])); // Expected: 1

console.log("\nTest Case 2:");
console.log("arr1 = [1, 5, 3, 6, 7], arr2 = [4, 3, 1]");
console.log("Result:", makeArrayIncreasing([1, 5, 3, 6, 7], [4, 3, 1])); // Expected: 2

console.log("\nTest Case 3:");
console.log("arr1 = [1, 5, 3, 6, 7], arr2 = [1, 6, 3, 3]");
console.log("Result:", makeArrayIncreasing([1, 5, 3, 6, 7], [1, 6, 3, 3])); // Expected: -1


