class Solution
{
public:
    bool checkStraightLine(vector<vector<int>> &coordinates)
    {
        int n = coordinates.size();
        int d_y = coordinates[1][1] - coordinates[0][1]; // y2-y1
        int d_x = coordinates[1][0] - coordinates[0][0]; // x2-x1
        // slope = d_y / dx
        for (int i = 2; i < n; i++)
        {
            int d_y_i = coordinates[i][1] - coordinates[0][1];
            int d_x_i = coordinates[i][0] - coordinates[0][0];
            // slope = d_y_i / d_x_i
            //  d_y_i * d_x = d_y * d_x_i => straight line
            if (d_y_i * d_x != d_y * d_x_i)
                return false;
        }
        return true;
    }
};