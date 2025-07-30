class Solution {
  getNSR(height) {
    // Initialize stack and result array
    const st = [];
    const n = height.length;
    const NSR = new Array(n);
    
    // Traverse from right to left
    for (let i = n - 1; i >= 0; i--) {
      // If stack is empty, no smaller element to the right
      if (st.length === 0) {
        NSR[i] = n;
      } 
      else {
        // Pop elements from stack while current height is <= top stack height
        while (st.length > 0 && height[st[st.length - 1]] >= height[i]) {
          st.pop();
        }
        // If stack becomes empty after popping
        if (st.length === 0) {
          NSR[i] = n;
        } 
        else {
          NSR[i] = st[st.length - 1];
        }
      }
      st.push(i); // Push current index to stack
    }
    return NSR;
  }

  getNSL(height) {
    const st = [];
    const n = height.length;
    const NSL = new Array(n);
    
    // Traverse from left to right
    for (let i = 0; i < n; i++) {
      // If stack is empty, no smaller element to the left
      if (st.length === 0) {
        NSL[i] = -1;
      } 
      else {
        // Pop elements from stack while current height is <= top stack height
        while (st.length > 0 && height[st[st.length - 1]] >= height[i]) {
          st.pop();
        }
        // If stack becomes empty after popping
        if (st.length === 0) {
          NSL[i] = -1;
        } 
        else {
          NSL[i] = st[st.length - 1];
        }
      }
      st.push(i); // Push current index to stack
    }
    return NSL;
  }

  findMaxArea(height) {
    // Get next smaller elements on right and left
    const NSR = this.getNSR(height);
    const NSL = this.getNSL(height);
    const n = height.length;
    const width = new Array(n);
    
    // Calculate width for each bar
    for (let i = 0; i < n; i++) {
      width[i] = NSR[i] - NSL[i] - 1;
    }
    
    // Find maximum area
    let maxArea = 0;
    for (let i = 0; i < n; i++) {
      const area = width[i] * height[i];
      maxArea = Math.max(maxArea, area);
    }
    return maxArea;
  }

  maximalRectangle(matrix) {
    if (!matrix || matrix.length === 0 || matrix[0].length === 0) {
      return 0;
    }
    
    const m = matrix.length;
    const n = matrix[0].length;
    const height = new Array(n).fill(0);
    let maxArea = 0;
    
    // Initialize height array with first row
    for (let i = 0; i < n; i++) {
      height[i] = matrix[0][i] === '1' ? 1 : 0;
    }
    maxArea = this.findMaxArea(height);
    
    // Process remaining rows
    for (let row = 1; row < m; row++) {
      for (let col = 0; col < n; col++) {
        // Update height: reset to 0 if '0', else increment
        height[col] = matrix[row][col] === '0' ? 0 : height[col] + 1;
      }
      // Update max area after processing each row
      maxArea = Math.max(maxArea, this.findMaxArea(height));
    }
    return maxArea;
  }
}

