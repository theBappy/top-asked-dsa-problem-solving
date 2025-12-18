var maxProfit = function (prices, strategy, k) {
    const n = prices.length;

    let actualProfit = 0;
    const profit = new Array(n);

    for (let i = 0; i < n; i++) {
        profit[i] = strategy[i] * prices[i];
        actualProfit += profit[i];
    }

    let originalWindowProfit = 0;
    let modifiedWindowProfit = 0;
    let maxGain = 0;

    let i = 0;

    for (let j = 0; j < n; j++) {
        originalWindowProfit += profit[j];

        // Second half of window
        if (j - i + 1 > Math.floor(k / 2)) {
            modifiedWindowProfit += prices[j];
        }

        // Shrink window
        if (j - i + 1 > k) {
            originalWindowProfit -= profit[i];
            modifiedWindowProfit -= prices[i + Math.floor(k / 2)];
            i++;
        }

        if (j - i + 1 === k) {
            maxGain = Math.max(
                maxGain,
                modifiedWindowProfit - originalWindowProfit
            );
        }
    }

    return actualProfit + maxGain;
};
