/**
 * @param {string[]} arr
 * @return {number}
 */
var maxLength = function(arr) {
    // Helper function to check for duplicates between two strings
    const hasDuplicate = (s1, s2) => {
        const charSet = new Set();
        
        // Check characters in s1
        for (const ch of s1) {
            if (charSet.has(ch)) return true;
            charSet.add(ch);
        }
        
        // Check characters in s2
        for (const ch of s2) {
            if (charSet.has(ch)) return true;
        }
        
        return false;
    };

    // Memoization map
    const memo = new Map();
    
    // Recursive solver function
    const solve = (i, currentStr) => {
        if (i >= arr.length) {
            return currentStr.length;
        }
        
        // Check memo first
        const memoKey = `${i}-${currentStr}`;
        if (memo.has(memoKey)) {
            return memo.get(memoKey);
        }
        
        let exclude = solve(i + 1, currentStr);
        let include = 0;
        
        if (!hasDuplicate(arr[i], currentStr)) {
            include = solve(i + 1, currentStr + arr[i]);
        }
        
        const result = Math.max(exclude, include);
        memo.set(memoKey, result);
        return result;
    };
    
    return solve(0, "");
};
