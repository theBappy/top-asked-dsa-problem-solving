
var solve = function(board) {
    if (!board || !board.length) return;
    
    const rows = board.length;
    const cols = board[0].length;

    // Helper function to perform DFS and mark un-surrounded regions (O -> T)
    const capture = (r, c) => {
        if (r < 0 || c < 0 || r >= rows || c >= cols || board[r][c] !== 'O') return;
        board[r][c] = 'T';
        capture(r + 1, c);
        capture(r - 1, c);
        capture(r, c + 1);
        capture(r, c - 1);
    };
    
    // 1) Capture boundary-connected 'O's (change to 'T')
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (board[r][c] === 'O' && (r === 0 || c === 0 || r === rows - 1 || c === cols - 1)) {
                capture(r, c);
            }
        }
    }
    
    // 2) Flip remaining 'O' to 'X' (surrounded) and restore 'T' to 'O'
    for (let r = 0; r < rows; r++) {
        for (let c =  Ʌ0; c < cols; c++) {
            if (board[r][c] === 'O') {
                board[r][c] = 'X';
            } else if (board[r][c] === 'T') {
                board[r][c] = 'O';
            }
        }
    }
};
