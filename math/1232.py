# Amazon

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
        n = len(coordinates)
        d_y =  coordinates[1][1] - coordinates[0][1]
        d_x = coordinates[1][0] - coordinates[0][0]
        for i in range(2, n):
            d_y_i = coordinates[i][1] - coordinates[0][1]
            d_x_i = coordinates[i][0] - coordinates[0][0]
            if d_y_i * d_x != d_y * d_x_i:
                return False
        return True
