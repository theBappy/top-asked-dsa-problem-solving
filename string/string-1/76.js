class Solution {
  minWindow(s, t) {
    const n = s.length;

    // Step 1: Build a frequency map for all characters in t
    const mp = {};
    for (const ch of t) {
      mp[ch] = (mp[ch] || 0) + 1;
    }

    // Step 2: Initialize variables
    let requiredCount = t.length; // total chars we still need
    let i = 0;                    // left pointer
    let j = 0;                    // right pointer
    let minStart = 0;             // start index of minimum window
    let minWindow = Infinity;     // length of smallest valid window

    // Step 3: Expand the right boundary of the window
    while (j < n) {
      const ch_j = s[j]; // current character at right pointer

      // If character is needed, reduce requiredCount
      if (mp[ch_j] !== undefined && mp[ch_j] > 0) {
        requiredCount--;
      }

      // Decrease the frequency count for the current character
      if (mp[ch_j] !== undefined) {
        mp[ch_j]--;
      } else {
        mp[ch_j] = -1; // for chars not in t
      }

      // Step 4: Try to shrink the window from the left when all chars are matched
      while (requiredCount === 0) {
        // Check if current window is smaller than the previous best
        if (minWindow > j - i + 1) {
          minWindow = j - i + 1;
          minStart = i;
        }

        const ch_i = s[i]; // leftmost character in current window

        // Restore its frequency since it's leaving the window
        if (mp[ch_i] !== undefined) {
          mp[ch_i]++;
          // If character becomes needed again, increment requiredCount
          if (mp[ch_i] > 0) {
            requiredCount++;
          }
        }
        i++; // move left pointer
      }

      // Step 5: Expand right pointer
      j++;
    }

    // Step 6: Return result
    return minWindow === Infinity ? "" : s.substring(minStart, minStart + minWindow);
  }
}

// Example usage:
// const sol = new Solution();
// console.log(sol.minWindow("ADOBECODEBANC", "ABC")); // Output: "BANC"
