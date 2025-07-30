// Time Complexity:
// - Building frequency map: O(n)
// - Sorting unique cards: O(k log k) where k is number of unique cards
// - Group formation: O(n) (each card processed exactly once)
// Total: O(n + k log k)
// Space Complexity:
// - Storage for count map: O(k) where k is number of unique cards
// - Storage for sorted array: O(k)
// Total: O(k)

function isNStraightHand(hand, groupSize) {
  // If total cards aren't divisible by groupSize, immediate fail
  if (hand.length % groupSize !== 0) {
    return false;
  }
  // Create frequency map of card counts
  const count = new Map();
  for (const num of hand) {
    count.set(num, (count.get(num) || 0) + 1);
  }
  // Get sorted unique card values
  const sortedCards = Array.from(count.keys()).sort((a, b) => a - b);
  for (const card of sortedCards) {
    // While we still have this card available
    while (count.get(card) > 0) {
      // Try to form a group starting with current card
      for (let i = 0; i < groupSize; i++) {
        const current = card + i;
        // If needed card is missing or exhausted
        if (!count.has(current) || count.get(current) === 0) {
          return false;
        }
        // Use one instance of this card
        count.set(current, count.get(current) - 1);
        // Clean up if count reaches zero
        if (count.get(current) === 0) {
          count.delete(current);
        }
      }
    }
  }
  return true;
}
