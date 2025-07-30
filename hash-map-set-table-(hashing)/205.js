//  Tc = O(n)
//  Sc = O(1) #128/256 ASCII Char(constant space)
class Solution {
  /**
   * @param {string} s
   * @param {string} t
   * @return {boolean}
   */
  isIsomorphic(s, t) {
    // Maps characters from string s to characters in string t
    const sToTMap = new Map();
    // Maps characters from string t to characters in string s (for bi-directional check)
    const tToSMap = new Map();

    const n = s.length; // Both strings must have the same length

    for (let i = 0; i < n; i++) {
      const charS = s[i];
      const charT = t[i];

      // Check mapping from s to t
      if (sToTMap.has(charS)) {
        // If charS is already mapped, ensure it maps to the same charT
        if (sToTMap.get(charS) !== charT) {
          return false;
        }
      } else {
        // If charS is not yet mapped, create the mapping
        sToTMap.set(charS, charT);
      }

      // Check mapping from t to s (crucial for bi-directional uniqueness)
      if (tToSMap.has(charT)) {
        // If charT is already mapped, ensure it maps back to the same charS
        if (tToSMap.get(charT) !== charS) {
          return false;
        }
      } else {
        // If charT is not yet mapped, create the reverse mapping
        tToSMap.set(charT, charS);
      }
    }

    return true;
  }
}
