class TilingSolver {
    constructor() {
        this.M = 1e9 + 7;
        this.memo = new Array(1001).fill(-1);
    }

    solve(n) {
        // Base cases
        if (n === 1 || n === 2) return n;
        if (n === 3) return 5;
        
        // Return memoized result if available
        if (this.memo[n] !== -1) return this.memo[n];
        
        // Recurrence relation: T(n) = 2*T(n-1) + T(n-3)
        this.memo[n] = (2 * this.solve(n - 1) % this.M + this.solve(n - 3) % this.M) % this.M;
        return this.memo[n];
    }

    numTilings(n) {
        return this.solve(n);
    }
}