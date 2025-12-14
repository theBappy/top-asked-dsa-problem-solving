/**
 * @param {string} corridor
 * @return {number}
 */
var numberOfWays = function (corridor) {
    const MOD = 1000000007n;
    const seats = [];

    for (let i = 0; i < corridor.length; i++) {
        if (corridor[i] === 'S') {
            seats.push(i);
        }
    }

    // Invalid cases
    if (seats.length === 0 || seats.length % 2 !== 0) {
        return 0;
    }

    let ways = 1n;

    // Start from the 3rd seat, jump by pairs
    for (let i = 2; i < seats.length; i += 2) {
        const gap = BigInt(seats[i] - seats[i - 1]);
        ways = (ways * gap) % MOD;
    }

    return Number(ways);
};
