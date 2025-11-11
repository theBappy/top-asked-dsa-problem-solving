var findMaxForm = function(strs, m, n) {
    let count = [];
    for (let s of strs) {
        let zeros = (s.match(/0/g) || []).length;
        let ones = (s.match(/1/g) || []).length;
        count.push([zeros, ones]);
    }
    

    let t = Array.from({ length: m + 1 }, () =>
        Array.from({ length: n + 1 }, () =>
            Array(count.length + 1).fill(-1)
        )
    );
    
    function solve(mm, nn, idx) {
        if (idx >= count.length || (mm === 0 && nn === 0)) {
            return 0;
        }
        if (t[mm][nn][idx] !== -1) {
            return t[mm][nn][idx];
        }
        
        let include = 0;
        if (count[idx][0] <= mm && count[idx][1] <= nn) {
            include = 1 + solve(mm - count[idx][0], nn - count[idx][1], idx + 1);
        }
        let exclude = solve(mm, nn, idx + 1);
        
        t[mm][nn][idx] = Math.max(include, exclude);
        return t[mm][nn][idx];
    }
    
    return solve(m, n, 0);
};
