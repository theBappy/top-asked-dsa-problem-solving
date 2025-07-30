// Function to transform the original string by inserting '#' between characters
function transform(s) {
    let temp = '#';
    for (let ch of s) {
        temp += ch + '#'; // Add character and another '#' after it
    }
    return temp;
}

// Main function to find the longest palindromic substring using Manacher’s Algorithm
function longestPalindrome(s) {
    const t = transform(s);         // Preprocessed string
    const n = t.length;             // Length of transformed string
    let l = 0, r = 0;               // Left and right boundaries of current palindrome
    let center = 0, maxLen = 0;     // To track center and length of longest palindrome
    const p = Array(n).fill(0);     // Array to store palindrome radii

    for (let i = 1; i < n; i++) {
        let k;

        if (i > r) {
            k = 0;                  // If outside current boundary, start fresh
        } else {
            let j = l + (r - i);    // Mirror index around current center
            if (j - p[j] > l) {
                p[i] = p[j];        // Safe to reuse mirror length
                continue;
            } else {
                k = r - i;          // Clip the expansion if near boundary
            }
        }

        // Expand palindrome centered at i
        while (i - k >= 0 && i + k < n && t[i - k] === t[i + k]) {
            k++;
        }
        k--;                        // Roll back last expansion attempt

        p[i] = k;                   // Save max expansion for center i

        // Update if we found a longer palindrome
        if (p[i] > maxLen) {
            maxLen = p[i];
            center = i;
        }

        // Update current palindrome boundary
        if (i + k > r) {
            l = i - k;
            r = i + k;
        }
    }

    const start = Math.floor((center - maxLen) / 2);   // Convert center index to original string index
    return s.slice(start, start + maxLen);             // Extract substring from original string
}
