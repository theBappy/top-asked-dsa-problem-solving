

/**
 * @param {number[]} derived
 * @return {boolean}
 */
var doesValidArrayExist = function (derived) {
    const n = derived.length;

    const original = new Array(n).fill(0);
    original[0] = 0;
    for (let i = 0; i < n - 1; i++) {
        original[i + 1] = original[i] ^ derived[i];
    }
    if ((original[n - 1] ^ original[0]) === derived[n - 1]) {
        return true;
    }

    original[0] = 1;
    for (let i = 0; i < n - 1; i++) {
        original[i + 1] = original[i] ^ derived[i];
    }
    if ((original[n - 1] ^ original[0]) === derived[n - 1]) {
        return true;
    }
    return false;
};



var doesValidArrayExist = function (derived) {
    let xor = 0
    for (let x of derived) {
        xor = xor ^ x
    }
    return xor === 0

};