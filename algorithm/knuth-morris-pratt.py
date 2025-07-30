# Tc = O(n+m) n = for searching through the txt length and m for LPS array of patter
# Sc = O(m) for storing LPS pattern array

class Solution:
    def computeLPS(self, pat: str, LPS: list, M: int) -> None:
        len = 0  # Length of the previous longest prefix suffix
        LPS[0] = 0  # LPS[0] is always 0
        i = 1  # Start from the second character
        # Loop to fill the LPS array
        while i < M:
            if pat[i] == pat[len]:  # Characters match
                len += 1
                LPS[i] = len  # Set LPS value
                i += 1
            else:
                if len != 0:  # Mismatch after len matches
                    len = LPS[len - 1]  # Use the previous LPS value
                else:
                    LPS[i] = 0  # No match found
                    i += 1
    def search(self, pat: str, txt: str) -> list:
        N = len(txt)  # Length of the text
        M = len(pat)  # Length of the pattern
        result = []  # List to store the result indices
        LPS = [0] * M  # Initialize LPS array
        self.computeLPS(pat, LPS, M)  # Compute the LPS array
        
        i = 0  # Index for text
        j = 0  # Index for pattern
        while i < N:
            if txt[i] == pat[j]:  # Characters match
                i += 1
                j += 1
            
            if j == M:  # A match is found
                result.append(i - M)  # Store the starting index
                j = LPS[j - 1]  # Get the next character to match
            elif i < N and txt[i] != pat[j]:  # Mismatch after j matches
                if j != 0:
                    j = LPS[j - 1]  # Use the previous LPS value
                else:
                    i += 1  # Move to the next character in text
        
        return result  # Return the list of starting indices


