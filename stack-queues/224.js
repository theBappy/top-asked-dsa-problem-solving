//  Tc = O(n)
//  Sc = O(n)
class Solution {
  calculate(s) {
    // Initialize variables:
    const n = s.length;    // Store length of input string
    const stack = [];      // Stack to handle parentheses operations
    let number = 0;        // Temporary storage for multi-digit numbers
    let result = 0;       // Accumulates total result
    let sign = 1;         // Tracks current sign (+1 or -1)

    // Process each character in the string:
    for (let i = 0; i < n; i++) {
      const char = s[i];  // Current character being processed

      if (char >= '0' && char <= '9') {
        // Build multi-digit number:
        number = number * 10 + parseInt(char);
      } 
      else if (char === '+') {
        // Add completed number to result with current sign:
        result += number * sign;
        number = 0;      // Reset number storage
        sign = 1;        // Set sign to positive
      } 
      else if (char === '-') {
        // Add completed number to result with current sign:
        result += number * sign;
        number = 0;      // Reset number storage
        sign = -1;       // Set sign to negative
      } 
      else if (char === '(') {
        // Push current context to stack before entering parentheses:
        stack.push(result);  // Save intermediate result
        stack.push(sign);    // Save current sign
        // Reset context for new parentheses block:
        result = 0;
        number = 0;
        sign = 1;
      } 
      else if (char === ')') {
        // Finalize current parentheses block:
        result += number * sign;  // Add last number in block
        number = 0;
        // Restore context from before parentheses:
        const stackSign = stack.pop();   // Retrieve saved sign
        const prevResult = stack.pop();  // Retrieve saved result
        result *= stackSign;            // Apply sign to current block
        result += prevResult;           // Combine with previous result
      }
      // Note: We silently skip spaces/whitespace
    }

    // Add any remaining number at end of string:
    result += number * sign;
    
    return result;
  }
}

