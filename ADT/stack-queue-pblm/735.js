/**
 * @param {number[]} asteroids
 * @return {number[]}
 */
var asteroidCollision = function (asteroids) {
    const st = []
    for (let a of asteroids) {
        while (st.length > 0 && a < 0 && st[st.length - 1] > 0) {
            const sum = a + st[st.length - 1]
            if (sum < 0) {
                st.pop()
            } else if (sum > 0) {
                a = 0
            } else {
                st.pop()
                a = 0
            }
        }
        if (a !== 0) {
            st.push(a)
        }
    }
    return st
};