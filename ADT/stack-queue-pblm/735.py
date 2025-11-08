class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for a in asteroids:
            while st and a < 0 and st[-1] > 0:
                sum_ = a + st[-1]
                if sum_ < 0:
                    st.pop()
                elif sum_ > 0:
                    a = 0
                else:
                    st.pop()
                    a = 0
            if a != 0:
                st.append(a)
        return st
