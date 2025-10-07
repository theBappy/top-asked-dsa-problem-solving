

function avoidFlood(rains) {
    const n = rains.length;
    const lakeMap = new Map(); // lake -> last day it was filled
    const dryDays = []; // indices of dry days (rains[day] == 0)
    const ans = new Array(n).fill(1); // default all dry days to dry lake 1

    // Helper function for binary search (bisect_left)
    function bisectLeft(arr, target) {
        let left = 0, right = arr.length;
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (arr[mid] < target) left = mid + 1;
            else right = mid;
        }
        return left;
    }

    for (let day = 0; day < n; day++) {
        const lake = rains[day];

        if (lake === 0) {
            dryDays.push(day); // record this dry day
        } else {
            ans[day] = -1; // raining day — can't dry any lake

            if (lakeMap.has(lake)) {
                // lake already filled previously
                const lastFilled = lakeMap.get(lake);
                // find the next dry day after it was last filled
                const i = bisectLeft(dryDays, lastFilled + 1);

                if (i === dryDays.length) {
                    // no dry day available to empty this lake before raining again → flood
                    return [];
                }

                const dryDay = dryDays.splice(i, 1)[0];
                ans[dryDay] = lake; // use this dry day to dry the lake
            }

            lakeMap.set(lake, day); // record latest day this lake was filled
        }
    }

    return ans;
}