var maximizeSquareArea = function (m, n, hFences, vFences) {
    const MOD = 1_000_000_007;

    hFences.push(1, m);
    vFences.push(1, n);

    hFences.sort((a, b) => a - b);
    vFences.sort((a, b) => a - b);

    // Store all vertical differences
    const vDiffs = new Set();
    for (let i = 0; i < vFences.length; i++) {
        for (let j = i + 1; j < vFences.length; j++) {
            vDiffs.add(vFences[j] - vFences[i]);
        }
    }

    let maxSide = 0;

    // Try horizontal differences (larger first)
    for (let i = 0; i < hFences.length; i++) {
        for (let j = i + 1; j < hFences.length; j++) {
            const diff = hFences[j] - hFences[i];
            if (vDiffs.has(diff)) {
                maxSide = Math.max(maxSide, diff);
            }
        }
    }

    if (maxSide === 0) return -1;

    return Number((BigInt(maxSide) * BigInt(maxSide)) % BigInt(MOD));
};
