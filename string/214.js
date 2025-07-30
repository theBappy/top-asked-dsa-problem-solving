
// Tc = O(n^2)
// Sc = O(n)

class Solution {
  computeLPS(pattern) {
    const M = pattern.length;
    const LPS = new Array(M).fill(0);
    let len = 0;  // Length of the previous longest prefix suffix
    let i = 1;

    while (i < M) {
      if (pattern[i] === pattern[len]) {  // Match found
        len++;
        LPS[i] = len;
        i++;
      } else {  // Mismatch
        if (len !== 0) {  // Try to find a smaller prefix that matches
          len = LPS[len - 1];
        } else {  // No smaller prefix matches
          LPS[i] = 0;
          i++;
        }
      }
    }
    return LPS;
  }

  shortestPalindrome(s) {
    const rev = s.split('').reverse().join('');  // Reverse the string
    const temp = s + '-' + rev;  // Concatenate original + separator + reversed
    const LPS = this.computeLPS(temp);  // Compute LPS array
    const longestLPSLength = LPS[temp.length - 1];  // Length of longest palindromic prefix
    const culprit = rev.slice(0, s.length - longestLPSLength);  // Characters to prepend
    return culprit + s;  // Shortest palindrome
  }
}

// Example usage:
const sol = new Solution();
console.log(sol.shortestPalindrome("aacecaaa"));  // Output: "aaacecaaa"



// Tc = O(n^2)
// Sc = O(n)
class Solution {
    shortestPalindrome(s) {
        const rev = s.split('').reverse().join(''); // Reverse the string
        for (let i = 0; i < s.length; i++) {
            // Check if the prefix of s matches the suffix of rev
            if (s.substring(0, s.length - i) === rev.substring(i)) {
                return rev.substring(0, i) + s; // Prepend non-matching part
            }
        }
        return rev + s; // If no match found, return full reversed + original
    }
}

// Example usage:
const solution = new Solution();
console.log(solution.shortestPalindrome("aacecaaa")); 