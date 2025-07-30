function findMedianSortedArrays(nums1, nums2) {
    // Ensure nums1 is the smaller array to optimize binary search
    if (nums1.length > nums2.length) {
        return findMedianSortedArrays(nums2, nums1);
    }
    
    const m = nums1.length;  // Size of smaller array (nums1)
    const n = nums2.length;  // Size of larger array (nums2)
    let left = 0;
    let right = m;
    
    // Perform binary search on the smaller array (nums1)
    while (left <= right) {
        // Partition position in nums1
        const partitionX = Math.floor((left + right) / 2);
        // Partition position in nums2 (calculated to balance total left elements)
        const partitionY = Math.floor((m + n + 1) / 2) - partitionX;
        
        // Handle edge cases where partition might be at start/end of arrays
        // Max of left partition (or -Infinity if no elements on left)
        const maxLeftX = (partitionX === 0) ? -Infinity : nums1[partitionX - 1];
        const maxLeftY = (partitionY === 0) ? -Infinity : nums2[partitionY - 1];
        
        // Min of right partition (or +Infinity if no elements on right)
        const minRightX = (partitionX === m) ? Infinity : nums1[partitionX];
        const minRightY = (partitionY === n) ? Infinity : nums2[partitionY];
        
        // Check if we've found the correct partition
        if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
            // If total length is odd, return max of left partitions
            if ((m + n) % 2 === 1) {
                return Math.max(maxLeftX, maxLeftY);
            }
            // If even, return average of max left and min right
            return (Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2;
        } else if (maxLeftX > minRightY) {
            // Need to move partition left in nums1
            right = partitionX - 1;
        } else {
            // Need to move partition right in nums1
            left = partitionX + 1;
        }
    }
    
    // Should never reach here for valid inputs
    throw new Error("Input arrays are not sorted");
}

// Example usage:
const nums1 = [1, 3, 5];
const nums2 = [2, 4, 6];
console.log(findMedianSortedArrays(nums1, nums2));  // Output: 3.5

// Tc = O(log(min(m,n))) [binary search performed on smaller array]
// Sc = O(1) [no additional data structure used]