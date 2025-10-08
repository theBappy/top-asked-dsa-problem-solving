//Approach-1 : Using lower_bound STL
//T.C : O(n log n + m log n)
//S.C : O(1)
class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        int m = spells.size();
        
        int n = potions.size();
        
        //O(n * logn)
        sort(begin(potions), end(potions));
        
        int maxPotion = potions[n-1];
        
        vector<int> answer;
        
        //O(m * logm)
        for(int i = 0; i<m; i++) {
            
            int spell = spells[i];
            
            long long minPotion = ceil((1.0*success)/spell);
            
            if(minPotion > maxPotion) {
                answer.push_back(0);
                continue;
            }
            
            int index = lower_bound(begin(potions), end(potions), minPotion) - begin(potions);
            
            answer.push_back(n-index);
            
        }
        
        return answer;
    }
};

// implementing own lower bound
// Tc = O(n log n + m log n)
// Sc = O(1) or O(m) [including the result array]
class Solution {
public:
    int lowerBound(int l, int r, vector<int>& potions, int minPotion) {
        int possibleIndex = -1;
        int mid = 0;
        while (l <= r) {
            mid = l + (r - l) / 2;
            if (potions[mid] >= minPotion) {
                possibleIndex = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return possibleIndex;
    }
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions,
                                long long success) {
        int m = spells.size();

        int n = potions.size();

        sort(begin(potions), end(potions));

        int maxPotion = potions[n - 1];

        vector<int> answer;

        for (int i = 0; i < m; i++) {

            int spell = spells[i];

            long long minPotion = ceil((1.0 * success) / spell);

            if (minPotion > maxPotion) {
                answer.push_back(0);
                continue;
            }

            int index = lowerBound(0, n - 1, potions, minPotion);

            answer.push_back(n - index);
        }

        return answer;
    }
};
