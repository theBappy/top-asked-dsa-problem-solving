var countUnguarded = function (m, n, guards, walls) {
  const mark_guarded = (row, col, grid) => {
    for (let i = row - 1; i >= 0; i--) {
      if (grid[i][col] === 2 || grid[i][col] === 3) {
        break;
      }
      grid[i][col] = 1;
    }
    for (let i = row + 1; i < grid.length; i++) {
      if (grid[i][col] === 2 || grid[i][col] === 3) {
        break;
      }
      grid[i][col] = 1;
    }
    for (let j = col - 1; j >= 0; j--) {
      if (grid[row][j] === 2 || grid[row][j] === 3) {
        break;
      }
      grid[row][j] = 1;
    }
    for (let j = col + 1; j < grid[0].length; j++) {
      if (grid[row][j] === 2 || grid[row][j] === 3) {
        break;
      }
      grid[row][j] = 1;
    }
  };
  const grid = Array.from({ length: m }, () => Array(n).fill(0));
  for (const [i, j] of guards) {
    grid[i][j] = 2;
  }
  for (const [i, j] of walls) {
    grid[i][j] = 3;
  }
  for (const [i, j] of guards) {
    mark_guarded(i, j, grid);
  }
  let count = 0;
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === 0) {
        count++;
      }
    }
  }
  return count;
};
