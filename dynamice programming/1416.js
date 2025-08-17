const numberOfArrays = (s, k) => {
    const n = s.length;
    const mod = 1e9 + 7;
    const memo = new Array(n).fill(-1);

    const solve = (start) => {
        if (start >= n) return 1;
        if (memo[start] !== -1) return memo[start];
        if (s[start] === '0') return 0; // No leading zeros allowed

        let count = 0;
        let num = 0;

        for (let end = start; end < n; end++) {
            num = num * 10 + parseInt(s[end]);
            if (num > k) break;
            count = (count + solve(end + 1)) % mod;
        }

        return memo[start] = count;
    };

    return solve(0);
};

// Example usage:
console.log(numberOfArrays("1234", 100)); // Example output
console.log(numberOfArrays("1234567890", 90)); // Another example
