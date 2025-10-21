class Solution {
  /**
   * @param {number[][]} matrix
   * @param {number} target
   * @return {number}
   */
  numSubmatrixSumTarget(matrix, target) {
    const rows = matrix.length;
    if (rows === 0) return 0;
    const cols = matrix[0].length;

    // Preprocessing: Compute prefix sums for each row
    for (let row = 0; row < rows; row++) {
      for (let col = 1; col < cols; col++) {
        matrix[row][col] += matrix[row][col - 1];
      }
    }

    let result = 0;
    for (let startCol = 0; startCol < cols; startCol++) {
      for (let currCol = startCol; currCol < cols; currCol++) {
        const mp = new Map();
        mp.set(0, 1);
        let sumVal = 0;
        for (let row = 0; row < rows; row++) {
          // Calculate the sum for the sub-row from startCol to currCol
          sumVal +=
            matrix[row][currCol] -
            (startCol > 0 ? matrix[row][startCol - 1] : 0);

          // Check if (sumVal - target) exists in the map
          if (mp.has(sumVal - target)) {
            result += mp.get(sumVal - target);
          }

          // Update the map with the current sumVal
          mp.set(sumVal, (mp.get(sumVal) || 0) + 1);
        }
      }
    }

    return result;
  }
}
