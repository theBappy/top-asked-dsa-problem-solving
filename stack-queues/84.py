# Tc = O(n)
# Sc = O(n)
class Solution(object):
    def getNSR(self, height):
        st = []
        n = len(height)
        NSR = [0] * n
        for i in range(n-1, -1,-1):
            if not st:
                NSR[i] = n
            else:
                while st and height[st[-1]] >= height[i]:
                    st.pop()
                if not st:
                    NSR[i] = n
                else:
                    NSR[i] = st[-1]
            st.append(i)
        return NSR
    def getNSL(self, height):
        st = []
        n = len(height)
        NSL = [0] * n
        for i in range(n):
            if not st:
                NSL[i] = -1
            else:
                while st and height[st[-1]] >= height[i]:
                    st.pop()
                if not st:
                    NSL[i] = -1
                else:
                    NSL[i] = st[-1]
            st.append(i)
        return NSL
    def largestRectangleArea(self, height):
        NSR = self.getNSR(height)
        NSL = self.getNSL(height)
        n = len(height)
        width = [0] * n
        for i in range(n):
            width[i] = NSR[i] - NSL[i] - 1
        maxArea = 0
        for i in range(n):
            area = width[i] * height[i] 
            maxArea = max(maxArea, area)
        return maxArea
        
        