# Tc = O(m + n)
# Sc = O(n)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Length of the main string
        n = len(s)

        # Build a frequency map (instead of Counter) for all characters in t
        mp = {}
        for ch in t:
            mp[ch] = mp.get(ch, 0) + 1

        # Total number of characters we still need to find
        requiredCount = len(t)

        # Initialize sliding window pointers and minimum window tracking variables
        i = 0
        j = 0
        minStart = 0
        minWindow = float('inf')

        # Expand the right boundary of the window
        while j < n:
            ch_j = s[j]  # Current character at right pointer

            # If current character is still needed, reduce the count of required characters
            if ch_j in mp and mp[ch_j] > 0:
                requiredCount -= 1

            # Decrease frequency count (can go below zero if character appears extra times)
            if ch_j in mp:
                mp[ch_j] -= 1
            else:
                mp[ch_j] = -1  # handle characters not in t

            # When all required characters are matched, try to shrink the window
            while requiredCount == 0:
                # Update the minimum window if the current one is smaller
                if minWindow > j - i + 1:
                    minWindow = j - i + 1
                    minStart = i

                # Try to move the left pointer to shrink the window
                ch_i = s[i]

                # Restore the frequency of the left character since it’s going out of the window
                if ch_i in mp:
                    mp[ch_i] += 1
                    # If this character becomes needed again, increase requiredCount
                    if mp[ch_i] > 0:
                        requiredCount += 1
                i += 1  # move left pointer

            # Move right pointer to expand the window
            j += 1

        # If no valid window found, return empty string
        return "" if minWindow == float('inf') else s[minStart:minStart + minWindow]

