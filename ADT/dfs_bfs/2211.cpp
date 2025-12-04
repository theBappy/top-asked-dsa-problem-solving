class Solution {
public:
    int countCollisions(string directions) {
        int n = directions.length();
        int i = 0; // left boundary
        while (i < n && directions[i] == 'L') {
            i++;
        }
        int j = n - 1; //right boundary
        while (j >= 0 && directions[j] == 'R') {
            j--;
        }
        int collisions = 0;
        while (i <= j) {
            if (directions[i] != 'S') {
                collisions++;
            }
            i++;
        }
        return collisions;
    }
};