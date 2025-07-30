//  Tc = O(n)
//  SC = O(n) [fot the set]

class Solution {
  longestConsecutive(nums) {
    // Convert the array to a Set for O(1) average time complexity lookups.
    const numsSet = new Set(nums);
    let maxLen = 0; // Initialize the maximum consecutive sequence length found

    // Iterate through each number in the set
    for (const num of numsSet) {
      // Check if the current number is the start of a sequence.
      // A number `num` is the start of a sequence if `num - 1` is NOT in the set.
      if (!numsSet.has(num - 1)) {
        let currNum = num; // Start of the current consecutive sequence
        let currLen = 1; // Length of the current consecutive sequence

        // While the next consecutive number exists in the set, continue extending the sequence
        while (numsSet.has(currNum + 1)) {
          currNum += 1; // Move to the next number in the sequence
          currLen += 1; // Increment the current sequence length
        }

        // Update the overall maximum length found so far
        maxLen = Math.max(currLen, maxLen);
      }
    }

    return maxLen; // Return the maximum consecutive sequence length
  }
}
