// T.C : O(V^3)
// S.C : O(V^2)

class Solution
{
public:
#define P pair<int, int>
    void floydWarshall(int n, vector<vector<int>> &shortestPathMatrix)
    {

        for (int via = 0; via < n; via++)
        {

            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {

                    shortestPathMatrix[i][j] = min(shortestPathMatrix[i][j],
                                                   shortestPathMatrix[i][via] + shortestPathMatrix[via][j]);
                }
            }
        }
    }

    int getCityWithFewestReachable(int n, const vector<vector<int>> &shortestPathMatrix, int distanceThreshold)
    {
        int cityWithFewestReachable = -1;
        int fewestReachableCount = INT_MAX;

        for (int i = 0; i < n; i++)
        {
            int reachableCount = 0;
            for (int j = 0; j < n; j++)
            {
                if (i != j && shortestPathMatrix[i][j] <= distanceThreshold)
                {
                    reachableCount++;
                }
            }

            if (reachableCount <= fewestReachableCount)
            {
                fewestReachableCount = reachableCount;
                cityWithFewestReachable = i;
            }
        }
        return cityWithFewestReachable;
    }

    int findTheCity(int n, vector<vector<int>> &edges, int distanceThreshold)
    {
        vector<vector<int>> shortestPathMatrix(n, vector<int>(n, 1e9 + 7));

        for (int i = 0; i < n; i++)
        {
            shortestPathMatrix[i][i] = 0; // Distance to itself is zero
        }

        for (const auto &edge : edges)
        {
            int u = edge[0];
            int v = edge[1];
            int wt = edge[2];
            shortestPathMatrix[u][v] = wt;
            shortestPathMatrix[v][u] = wt;
        }

        floydWarshall(n, shortestPathMatrix);

        return getCityWithFewestReachable(n, shortestPathMatrix, distanceThreshold);
    }
};