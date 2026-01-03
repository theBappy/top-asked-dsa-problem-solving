var numOfWays = function (n) {
    const M = 1000000007;
    const states = ["RYG", "RGY", "RYR", "RGR", "YRG", "YGR", "YGY", "YRY", "GRY", "GYR", "GRG", "GYG"];
    const t = Array.from({ length: n + 1 }, () => Array(12).fill(-1));

    function solve(remaining, prev) {
        if (remaining === 0) return 1;

        if (t[remaining][prev] !== -1) return t[remaining][prev];

        let result = 0;
        const last = states[prev];

        for (let curr = 0; curr < 12; curr++) {
            if (curr === prev) continue;

            const currPat = states[curr];
            let conflict = false;
            for (let col = 0; col < 3; col++) {
                if (currPat[col] === last[col]) {
                    conflict = true;
                    break;
                }
            }

            if (!conflict) {
                result = (result + solve(remaining - 1, curr)) % M;
            }
        }

        t[remaining][prev] = result;
        return result;
    }

    let result = 0;
    for (let i = 0; i < 12; i++) {
        result = (result + solve(n - 1, i)) % M;
    }

    return result;
};