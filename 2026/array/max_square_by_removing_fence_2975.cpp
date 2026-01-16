// Using hashset to store possible sides
// T.C : O(h^2 + v^2 + hlogh + vlogv), h = hFences.size(), v = vFences.size()
// S.C : O(h+v)

class Solution {
public:
    int M = 1e9+7;
    int maximizeSquareArea(int m, int n, vector<int>& hFences, vector<int>& vFences) {
        hFences.push_back(1);
        hFences.push_back(m);

        vFences.push_back(1);
        vFences.push_back(n);

        sort(begin(hFences), end(hFences)); 
        sort(begin(vFences), end(vFences));

        unordered_set<int> widths;
        unordered_set<int> heights;

        for(int i = 0; i < vFences.size(); i++) {
            for(int j = i+1; j < vFences.size(); j++) {
                int width = vFences[j] - vFences[i];
                widths.insert(width);
            }
        }

        int maxSide = 0;

        for(int i = 0; i < hFences.size(); i++) {
            for(int j = i+1; j < hFences.size(); j++) {
                int height = hFences[j] - hFences[i];
                if(widths.find(height) != widths.end()) { //found a square
                    maxSide = max(maxSide, height);
                }
            }
        }

        return maxSide == 0 ? -1 : (1LL * maxSide * maxSide) % M;

        
    }
};