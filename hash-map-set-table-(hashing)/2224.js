class Solution {
    findWinners(matches) {
        const lostCount = new Map();
        for (const [winner, loser] of matches) {
            if (!lostCount.has(winner)) {
                lostCount.set(winner, 0);
            }
            lostCount.set(loser, (lostCount.get(loser) || 0) + 1);
        }
        const notLost = [];
        const onceLost = [];
        for (const player of lostCount.keys()) {
            if (lostCount.get(player) === 0) {
                notLost.push(player);
            } else if (lostCount.get(player) === 1) {
                onceLost.push(player);
            }
        }
        return [notLost.sort((a, b) => a - b), onceLost.sort((a, b) => a - b)];
    }
}