class Solution {
    computeLPS(pat, LPS) {
        let M = pat.length
        let len = 0; // Length of the previous longest prefix suffix
        LPS[0] = 0;  // LPS[0] is always 0
        let i = 1;   // Start from the second character

        // Loop to fill the LPS array
        while (i < M) {
            if (pat[i] === pat[len]) { // Characters match
                len++;
                LPS[i] = len; // Set LPS value
                i++;
            } else {
                if (len !== 0) { // Mismatch after len matches
                    len = LPS[len - 1]; // Use the previous LPS value
                } else {
                    LPS[i] = 0; // No match found
                    i++;
                }
            }
        }
    }

    search(pat, txt) {
        const N = txt.length; // Length of the text
        const M = pat.length; // Length of the pattern
        
        const result = []; // Array to store the result indices
        const LPS = new Array(M).fill(0); // Initialize LPS array
        this.computeLPS(pat, LPS); // Compute the LPS array
        
        let i = 0; // Index for text
        let j = 0; // Index for pattern
        while (i < N) {
            if (txt[i] === pat[j]) { // Characters match
                i++;
                j++;
            }
            
            if (j === M) { // A match is found
                result.push(i - M); // Store the starting index
                j = LPS[j - 1]; // Get the next character to match
            } else if (i < N && txt[i] !== pat[j]) { // Mismatch after j matches
                if (j !== 0) {
                    j = LPS[j - 1]; // Use the previous LPS value
                } else {
                    i++; // Move to the next character in text
                }
            }
        }
        
        return result; // Return the list of starting indices
    }
}
