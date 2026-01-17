// Just find all possible intersections and best square side from them
// T.C : O(n * n)
// S.C : O(1)
class Solution {
public:
    long long largestSquareArea(vector<vector<int>>& bottomLeft, vector<vector<int>>& topRight) {
        int n = bottomLeft.size(); //topRight.size()

        int maxSide = 0;

        for(int i = 0; i < n; i++) {
            for(int j = i+1; j < n; j++) {
                //Width
                int topRightX   = min(topRight[i][0], topRight[j][0]);
                int bottomLeftX = max(bottomLeft[i][0], bottomLeft[j][0]);

                int width = topRightX - bottomLeftX;

                //Height
                int topRightY   = min(topRight[i][1], topRight[j][1]);
                int bottomLeftY = max(bottomLeft[i][1], bottomLeft[j][1]);

                int height = topRightY - bottomLeftY;

                int side = min(width, height);

                maxSide = max(maxSide, side);
            }
        }

        return 1LL * maxSide*maxSide;
    }
};
