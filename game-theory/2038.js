

/**
 * @param {string} colors
 * @return {boolean}
 */
var winnerOfGame = function (colors) {
        const n = colors.length;
        let alice = 0;
        let bob = 0;
        for (let i = 1; i < n - 1; i++) {
            if (colors[i - 1] === colors[i] && colors[i + 1] === colors[i]) {
                if (colors[i] === 'A') {
                    alice += 1;
                } else {
                    bob += 1;
                }
            }
        }
        return alice > bob;
}