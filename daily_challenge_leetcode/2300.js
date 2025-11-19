// implementing own lower bound
// Tc = O(n log n + m log n)
// Sc = O(1) or O(m) [including the result array]

var successfulPairs = function (spells, potions, success) {
  const m = spells.length; // number of spells
  const n = potions.length; // number of potions

  potions.sort((a, b) => a - b); // sort potions in ascending order
  const maxPotion = potions[n - 1]; // largest potion value
  const answer = []; // stores number of successful pairs for each spell

  // 🔹 Helper function: binary search for first potion >= minPotion
  const lowerBound = (l, r, minPotion) => {
    let possibleIndex = -1;
    while (l <= r) {
      const mid = l + Math.floor((r - l) / 2); // midpoint

      if (potions[mid] >= minPotion) {
        possibleIndex = mid; // potential valid position
        r = mid - 1; // continue searching left for earlier valid potion
      } else {
        l = mid + 1; // search right
      }
    }
    return possibleIndex; // returns first valid index, or -1 if not found
  };

  // 🔹 For each spell, count how many potions form a successful pair
  for (let i = 0; i < m; i++) {
    const spell = spells[i];

    // minimum potion strength needed to reach or exceed success
    const minPotion = Math.ceil(success / spell);

    // if even the strongest potion is too weak, add 0
    if (minPotion > maxPotion) {
      answer.push(0);
      continue;
    }

    // binary search for the first potion >= minPotion
    const index = lowerBound(0, n - 1, minPotion);

    // if index === -1, no valid potions; otherwise count all from index → end
    answer.push(index === -1 ? 0 : n - index);
  }

  return answer;
};