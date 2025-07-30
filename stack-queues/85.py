# Tc = O(m.n)
# Sc = O(n)
class Solution:
    def getNSR(self, height):
        # Initialize a stack to keep track of indices
        st = []
        n = len(height)  # Get the number of columns
        NSR = [0] * n    # Initialize the Next Smaller Right (NSR) array

        # Traverse the height array from right to left
        for i in range(n - 1, -1, -1):
            # If the stack is empty, set NSR[i] to n (out of bounds)
            if not st:
                NSR[i] = n
            else:
                # Pop elements from the stack while the current height is less than or equal to the height at the index on top of the stack
                while st and height[st[-1]] >= height[i]:
                    st.pop()
                # If the stack is empty after popping, set NSR[i] to n
                if not st:
                    NSR[i] = n
                else:
                    # Otherwise, set NSR[i] to the index on top of the stack
                    NSR[i] = st[-1]
            # Push the current index onto the stack
            st.append(i)
        return NSR

    def getNSL(self, height):
        # Initialize a stack to keep track of indices
        st = []
        n = len(height)  # Get the number of columns
        NSL = [0] * n    # Initialize the Next Smaller Left (NSL) array

        # Traverse the height array from left to right
        for i in range(n):
            # If the stack is empty, set NSL[i] to -1 (out of bounds)
            if not st:
                NSL[i] = -1
            else:
                # Pop elements from the stack while the current height is less than or equal to the height at the index on top of the stack
                while st and height[st[-1]] >= height[i]:
                    st.pop()
                # If the stack is empty after popping, set NSL[i] to -1
                if not st:
                    NSL[i] = -1
                else:
                    # Otherwise, set NSL[i] to the index on top of the stack
                    NSL[i] = st[-1]
            # Push the current index onto the stack
            st.append(i)
        return NSL

    def findMaxArea(self, height):
        # Get the Next Smaller Right and Left indices
        NSR = self.getNSR(height)
        NSL = self.getNSL(height)

        n = len(height)  # Get the number of columns
        width = [0] * n  # Initialize the width array

        # Calculate the width for each column
        for i in range(n):
            width[i] = NSR[i] - NSL[i] - 1  # Width = NSR[i] - NSL[i] - 1

        maxArea = 0  # Initialize max area
        # Calculate the maximum area
        for i in range(n):
            area = width[i] * height[i]  # Area = width * height
            maxArea = max(maxArea, area)   # Update max area if the current area is larger

        return maxArea

    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:  # Check for empty matrix
            return 0

        m = len(matrix)  # Get the number of rows
        n = len(matrix[0])  # Get the number of columns
        height = [0] * n  # Initialize the height array

        # Build the height array for the first row
        for i in range(n):
            height[i] = 1 if matrix[0][i] == '1' else 0  # Set height based on the first row

        maxArea = self.findMaxArea(height)  # Calculate max area for the first row

        # Iterate through the remaining rows
        for row in range(1, m):
            for col in range(n):
                # Update the height array based on the current row
                if matrix[row][col] == '0':
                    height[col] = 0  # Reset height if '0'
                else:
                    height[col] += 1  # Increment height if '1'
            # Update max area with the area calculated for the current row
            maxArea = max(maxArea, self.findMaxArea(height))

        return maxArea  # Return the maximum area found
